from sentence_transformers import SentenceTransformer, util

class SemanticMatcher:
    def __init__(self, model_path="models/fine_tuned_matcher"):
        # This loads YOUR fine-tuned model instead of the generic base model!
        self.model = SentenceTransformer(model_path)

    def get_match_score(self, jd_text, resume_text):
        # Convert both texts into mathematical vectors (embeddings)
        jd_embedding = self.model.encode(jd_text, convert_to_tensor=True)
        resume_embedding = self.model.encode(resume_text, convert_to_tensor=True)
        
        # Calculate how close the two vectors are (Cosine Similarity)
        cosine_score = util.cos_sim(jd_embedding, resume_embedding).item()
        
        # Convert to a percentage out of 100
        match_percentage = round(cosine_score * 100, 2)
        
        # Ensure it stays cleanly between 0% and 100%
        return max(0, min(match_percentage, 100))