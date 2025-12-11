📹 Demo Video
The repository includes a demonstration video:
Ai Powered Resume Matcher.mp4



# 🧠 AI-Powered Resume Matcher
AI-Powered Resume Matcher using NLP &amp; Machine Learning. A Streamlit app that analyzes multiple resumes and compares them with a job description using Sentence-BERT embeddings, cosine similarity, and spaCy NLP preprocessing. Upload any PDF/DOCX/TXT resume and instantly get match scores with clean, interactive UI.

A simple yet powerful **Streamlit web application** that matches resumes to a job description using **semantic similarity** with Sentence-BERT and spaCy NLP.  
This tool helps recruiters, HR professionals, and students quickly evaluate how well each resume aligns with a given job description.

---

## 🚀 Features

- Upload multiple resumes (**PDF, DOCX, TXT**) at once  
- Paste any job description  
- Automatically extracts text from resumes  
- Cleans text using spaCy (lemmatization, stopword removal)  
- Generates embeddings using **SentenceTransformer (all-MiniLM-L6-v2)**  
- Computes similarity using **cosine similarity**  
- Displays match percentage for each resume  
- Clean, interactive **Streamlit UI**  

---

## 📂 Project Structure
📦 AI-Resume-Matcher
├── app.py # Streamlit web application
├── AI_Resume_Matcher.ipynb # Notebook version (for understanding logic)
├── requirements.txt # All dependencies
├── Ai Powered Resume Matcher.mp4 # Demo video
└── README.md # Project documentation


---

## 🛠️ Technologies Used

- **Python 3**  
- **Streamlit** – UI framework  
- **spaCy** – NLP preprocessing  
- **SentenceTransformer (SBERT)** – Embeddings  
- **PyMuPDF (fitz)** – PDF text extraction  
- **python-docx** – DOCX text extraction  

---

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/RTds1234/AI-Resume-Matcher.git  
cd AI-Resume-Matcher
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```
### 4. Run the Application
```bash
streamlit run app.py
```
📘 How It Works

1. User Input
Paste a job description
Upload one or more resumes

2. Text Extraction
PDF: Extracted using PyMuPDF
DOCX: Extracted using python-docx
TXT: Read directly

3. Text Cleaning
spaCy is used to:
Lowercase text
Remove stopwords
Remove punctuation
Apply lemmatization

4. Semantic Embeddings
SentenceTransformer generates embeddings for:
Job description
Each resume

5. Matching
Cosine similarity computes match score:
score = cos_sim(jd_embedding, resume_embedding) * 100
Then results are sorted high → low.

📊 Output Example
📊 Match Results  
-------------------------  
resume_john.pdf → 87% match  
resume_priya.docx → 74% match  
resume_rahul.pdf → 61% match  


📄 requirements.txt
spaCy
scikit-learn  
sentence-transformers  
pdfminer.six  
python-docx  
streamlit  
PyMuPDF


