import spacy

class SkillExtractor:
    def __init__(self, model_name="en_core_web_sm"):
        self.nlp = spacy.load(model_name)
        # Expanded list of generic corporate/fluff words
        self.ignore_words = {
            'plus', 'field', 'degree', 'environment', 'team', 'teams', 
            'strategies', 'deliverables', 'requirements', 'ability', 
            'years', 'experience', 'bachelor', 'proficiency', 'solutions',
            'responsibilities', 'clean', 'maintainable', 'client', 'key',
            'administration', 'scenarios', 'driven', 'problem', 'applications'
        }

    def extract_skills(self, text):
        doc = self.nlp(text)
        skills = set()
        
        for chunk in doc.noun_chunks:
            clean_tokens = [token.text.lower() for token in chunk if not token.is_stop and not token.is_punct]
            
            if clean_tokens and not any(word in clean_tokens for word in self.ignore_words):
                clean_phrase = " ".join(clean_tokens).strip()
                if 2 < len(clean_phrase) < 35:
                    skills.add(clean_phrase)
                    
        return skills

    def find_missing_skills(self, jd_text, resume_text):
        jd_skills = self.extract_skills(jd_text)
        resume_text_lower = resume_text.lower()
        
        missing = []
        for skill in jd_skills:
            # 1. Check for exact phrase match
            if skill not in resume_text_lower:
                
                # 2. Smart Fallback: Check if the most important words of the skill exist 
                # (e.g. if "microsoft excel" is the skill, check if "excel" is in the resume)
                skill_words = skill.split()
                # Find words longer than 4 chars (ignores 'and', 'with', etc.)
                core_words = [w for w in skill_words if len(w) > 4]
                
                # If there are core words, check if ANY of them are in the resume
                is_partially_matched = False
                if core_words:
                    for word in core_words:
                        if word in resume_text_lower:
                            is_partially_matched = True
                            break
                            
                if not is_partially_matched:
                    missing.append(skill)
                
        return sorted(missing)

def split_resume_sections(text):
    sections = {"experience": "", "skills": "", "education": ""}
    current_section = "experience"
    for line in text.split("\n"):
        lower_line = line.lower()
        if "skill" in lower_line:
            current_section = "skills"
        elif "education" in lower_line or "academic" in lower_line:
            current_section = "education"
        elif "experience" in lower_line or "work history" in lower_line:
            current_section = "experience"
        sections[current_section] += line + " "
    return {k: v.strip() for k, v in sections.items()}