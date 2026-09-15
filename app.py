import streamlit as st
from src.parser import extract_text_from_pdf, extract_text_from_docx
from src.extractor import SkillExtractor
from src.matcher import SemanticMatcher

# 1. Setup the Page
st.set_page_config(page_title="AI Resume Matcher", page_icon="📄", layout="wide")
st.title("📄 AI Resume-to-Job Semantic Matcher")
st.markdown("Upload a resume and paste a job description to see how well they match using our custom-trained AI.")

# 2. Cache the models so they don't reload every time you click a button
@st.cache_resource
def load_models():
    extractor = SkillExtractor()
    matcher = SemanticMatcher()
    return extractor, matcher

# Load them into memory
extractor, matcher = load_models()

# 3. Create the UI Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("1. Upload Resume")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf", "docx"])

with col2:
    st.header("2. Job Description")
    jd_text = st.text_area("Paste the job description here...", height=200)

# 4. The Analysis Logic
if st.button("Analyze Match", type="primary"):
    if uploaded_file is not None and jd_text.strip() != "":
        with st.spinner("Analyzing semantics and extracting skills..."):
            
            # Parse Resume
            if uploaded_file.name.endswith('.pdf'):
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_docx(uploaded_file)
            
            # Get Match Score from your fine-tuned model!
            match_score = matcher.get_match_score(jd_text, resume_text)
            
            # Get Missing Skills via spaCy
            missing_skills = extractor.find_missing_skills(jd_text, resume_text)
            
            # 5. Display the Results
            st.divider()
            st.header("📊 Analysis Results")
            
            res_col1, res_col2 = st.columns([1, 1])
            
            with res_col1:
                st.subheader("Semantic Match Score")
                if match_score >= 75:
                    st.success(f"## {match_score}% \nExcellent Match!")
                elif match_score >= 50:
                    st.warning(f"## {match_score}% \nGood Match.")
                else:
                    st.error(f"## {match_score}% \nNeeds Alignment.")
                    
            with res_col2:
                st.subheader("Missing Keywords / Skills")
                if missing_skills:
                    st.write("Consider adding these to your resume if you have experience with them:")
                    # Display the top 15 missing skills nicely formatted
                    st.markdown(', '.join([f"`{skill}`" for skill in missing_skills[:15]]))
                else:
                    st.success("Your resume covers the key terms well!")
                    
    else:
        st.warning("Please upload a resume and paste a job description first.")