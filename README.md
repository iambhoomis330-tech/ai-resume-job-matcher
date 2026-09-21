# 🤖 AI Resume Analyzer & Job Matcher

An AI-powered web application that analyzes resumes, compares them with job descriptions, identifies skill gaps, evaluates resume quality, and recommends suitable job roles.

Built with Python, NLP, Machine Learning, and Streamlit.

---

## 🚀 Features

### 📄 Resume Analysis

- Upload PDF or DOCX resumes
- Extract resume text automatically
- Detect technical skills
- Analyze resume structure
- Evaluate resume quality

### 🎯 Job Matching

- Compare resume with job descriptions
- TF-IDF based text similarity
- Skill-based matching
- Combined overall match score
- Match-level classification

### 🔎 Skill Gap Analysis

- Identify matching skills
- Identify missing skills
- Compare resume skills with job requirements
- Provide skill improvement recommendations

### 💼 Job Role Recommendation

Recommends suitable roles based on the skills detected in the resume.

Supported roles include:

- Data Scientist
- Data Analyst
- Machine Learning Engineer
- AI Engineer
- Data Engineer
- Web Developer
- Business Intelligence Analyst

### 📊 Dashboard

The Streamlit dashboard displays:

- Overall Match Score
- Match Level
- Skill Match Score
- Resume Quality Score
- Matching Skills
- Missing Skills
- Skill Comparison Chart
- Recommended Job Roles
- Resume Improvement Recommendations

---

## 🛠️ Tech Stack

**Programming:** Python

**Data Processing:** Pandas, NumPy

**Machine Learning:** Scikit-learn

**NLP:** TF-IDF, text processing

**Document Processing:** PyPDF2, python-docx

**Web Framework:** Streamlit

**Version Control:** Git, GitHub

---

## 🧠 How It Works

```text
Resume Upload
      ↓
Text Extraction
      ↓
Resume Skill Extraction
      ↓
Job Description Processing
      ↓
Skill Matching
      ↓
TF-IDF Text Similarity
      ↓
Combined Match Score
      ↓
Skill Gap Analysis
      ↓
Resume Quality Analysis
      ↓
Job Role Recommendation
      ↓
Personalized Recommendations
```

## 📊 Matching Methodology

The application uses two complementary approaches:

### 1. Text Similarity

TF-IDF converts resume and job-description text into numerical representations and cosine similarity measures how closely the texts match.

### 2. Skill Matching

The application identifies skills required by the job description and checks which of those skills are present in the resume.

The final score combines both approaches:

**- 40% Text Similarity**
**- 60% Skill Matching**

This provides a more meaningful job compatibility score than relying only on text similarity.

## 📁 Project Structure

```text
ai-resume-job-matcher/
│
├── app.py
├── resume_parser.py
├── resume_analyzer.py
├── skill_extractor.py
├── job_matcher.py
├── recommender.py
├── role_recommender.py
├── requirements.txt
├── .gitignore
│
├── data/
│ ├── skills.csv
│ └── job_roles.csv
│
└── uploads/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rinkitala-commits/ai-resume-job-matcher.git
```

Move into the project directory:

```bash
cd ai-resume-job-matcher
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

Then open:
http://localhost:8501

---

## 📝 Example Workflow

1. Upload your resume in PDF or DOCX format.
2. Paste a complete job description.
3. Click Analyze Resume.
4. Review the overall match score.
5. Check matching and missing skills.
6. Review resume quality.
7. Explore recommended job roles.
8. Use the recommendations to improve your resume.

---

## 🔐 Privacy

Uploaded resumes may contain personal information.

Resume uploads are intentionally excluded from Git using .gitignore.

Do not commit personal resumes, .env files, credentials, or other sensitive information to the repository.

---

## 🔮 Future Improvements

- LLM-powered resume feedback
- Named Entity Recognition for advanced resume parsing
- ATS compatibility analysis
- Resume keyword optimization
- Multiple job-description comparison
- Job recommendation based on resume
- Resume section quality scoring
- PDF resume report generation
- Cloud deployment
- User accounts and resume history

---
## 🌐 Live Demo

🚀 **Live Application:**  
https://ai-resume-job-matcher-alq2cazapx2fhzhonsqmrg.streamlit.app/

## 🔗 GitHub Repository

https://github.com/rinkitala-commits/ai-resume-job-matcher

---

## 👩‍💻 Author

### Jhumarani Tala

B.Tech Data Science Student | Python Developer | Data Science & AI Enthusiast

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
