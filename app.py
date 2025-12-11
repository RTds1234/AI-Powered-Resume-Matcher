import streamlit as st
import fitz  # PyMuPDF
import os
import docx  # for DOCX support
from sentence_transformers import SentenceTransformer, util
import spacy

# Load models
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer("all-MiniLM-L6-v2")

# --- Helper Functions ---
def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif file.name.endswith(".docx"):
        document = docx.Document(file)
        return "\n".join([para.text for para in document.paragraphs])
    elif file.name.endswith(".txt"):
        return str(file.read(), encoding="utf-8")
    else:
        return ""

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# --- Streamlit UI ---
st.set_page_config(page_title="AI Resume Matcher", layout="centered")
st.title("🧠 AI Resume Matcher")
st.write("Upload resumes and provide a job description to see how well each resume matches!")

# Job Description Input
jd_text = st.text_area("📄 Paste Job Description Here", height=200)

# Upload Resumes
uploaded_resumes = st.file_uploader("📎 Upload Resume(s)", type=["pdf", "docx", "txt"], accept_multiple_files=True)

# Match Logic
if st.button("🔍 Match Resumes") and jd_text and uploaded_resumes:
    with st.spinner("Analyzing resumes..."):
        jd_clean = clean_text(jd_text)
        jd_embedding = model.encode(jd_clean, convert_to_tensor=True)

        results = []
        for resume_file in uploaded_resumes:
            try:
                resume_text = extract_text(resume_file)
                resume_clean = clean_text(resume_text)
                resume_embedding = model.encode(resume_clean, convert_to_tensor=True)
                score = util.cos_sim(jd_embedding, resume_embedding).item() * 100
                results.append((resume_file.name, round(score, 2)))
            except Exception as e:
                st.warning(f"❌ Could not process {resume_file.name}: {e}")

        results.sort(key=lambda x: x[1], reverse=True)

        st.subheader("📊 Match Results")
        for name, score in results:
            st.write(f"✅ **{name}** → **{score}% match**")
else:
    st.info("Please paste a job description and upload at least one resume to start.")
