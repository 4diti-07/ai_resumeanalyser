# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Multi-Agent Workflows.

The application analyzes resumes, evaluates ATS compatibility, identifies missing skills, recommends projects, generates a learning roadmap, compares resumes against job descriptions, and produces a downloadable PDF report.

---

# Features

✅ Resume PDF Upload

✅ Resume Text Extraction (PyMuPDF)

✅ Retrieval-Augmented Generation (RAG)

✅ ChromaDB Vector Database

✅ HuggingFace Embeddings

✅ Multi-Agent AI Workflow

✅ ATS Analysis

✅ Skills Assessment

✅ Suggested Projects

✅ Career Recommendations

✅ Learning Roadmap

✅ Job Description Matching

✅ Downloadable PDF Report

---

# Tech Stack

Frontend
- Streamlit

Backend
- Python

LLM
- OpenAI / OpenRouter

Vector Database
- ChromaDB

Embeddings
- HuggingFace Sentence Transformers

Libraries
- LangChain
- PyMuPDF
- ReportLab
- Streamlit

---

# Project Structure

```text
resumeanalyser/

│── app.py
│── workflow.py
│── agent.py
│── llm.py
│── prompts.py
│── rag.py
│── embeddings.py
│── vectorstore.py
│── build_db.py
│── jd_matcher.py
│── report_generator.py
│── extracter.py
│── requirements.txt

│
├── knowledge_base/
│      ├──ATS_Resume_Optimization_Guide.pdf
│      ├─Resume_Writing_Career_Development_Handbook.pdf
│      ├── Technical_Skills_Handbook.pdf
│      ├── Embedded_Systems_IoT_Handbook.pdf
│      └── AI_ML_Projects_Interview_Handbook.pdf

│
├── chroma_db/

│
├── uploads/

│
└── reports/
```

# Workflow - how this works

1. User uploads a resume PDF.

2. Resume text is extracted using PyMuPDF.

3. Relevant information is retrieved from the knowledge base using RAG.

4. Retrieved context is passed to multiple AI agents.

5. Each agent performs a specialized analysis.

6. Results are combined into one comprehensive report.

7. User can compare the resume against a Job Description.

8. A downloadable PDF report is generated.

---

# AI Agents

### ATS Agent

Evaluates ATS compatibility.

---

### Skills Agent

Identifies strengths, weaknesses and missing technical skills.

---

### Projects Agent

Suggests projects that strengthen the resume.

---

### Career Agent

Provides career recommendations.

---

### Roadmap Agent

Creates a learning roadmap.

---

# Retrieval-Augmented Generation (RAG)

The application uses a custom knowledge base consisting of professional resume guides, technical handbooks, AI/ML resources and Embedded Systems documentation.

The knowledge base is indexed using:

- HuggingFace Embeddings
- ChromaDB

Relevant chunks are retrieved before every LLM request.

---

# Installation

Clone the repository

```bash
git clone YOUR_REPO_URL
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENAI_API_KEY=your_key_here
```

Build the vector database

```bash
python build_db.py
```

Run the application

```bash
streamlit run app.py
```

---

## Deployed: https://airesumeanalyser-w9vf3xbt3nnjlmaym8mfup.streamlit.app/