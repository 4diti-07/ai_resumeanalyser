# AI Resume Analyzer - Architecture

## Workflow

```text
                  Resume PDF
                       │
                       ▼
              PDF Text Extractor
                       │
                       ▼
                 Resume Text
                       │
                       ▼
              RAG Context Retrieval
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     Chroma Vector DB        Knowledge Base PDFs
          │
          ▼
     Relevant Context
          │
          ▼
    Multi-Agent Workflow
 ┌────────┬────────┬────────┬────────┬────────┐
 ▼        ▼        ▼        ▼        ▼
ATS    Skills   Projects  Career  Roadmap
Agent   Agent    Agent     Agent    Agent
 └────────┴────────┴────────┴────────┴────────┘
                      │
                      ▼
             Final Report Generator
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  Streamlit Dashboard        PDF Report
```

## Components

### 1. Resume Upload
Users upload their resume in PDF format.

### 2. Text Extraction
PyMuPDF extracts text from the uploaded resume.

### 3. Retrieval-Augmented Generation (RAG)
The resume is used to retrieve relevant information from the Chroma vector database built from curated career, ATS, AI, and IoT knowledge.

### 4. Multi-Agent Workflow
Five specialized agents independently analyze different aspects of the resume:
- ATS Agent
- Skills Agent
- Projects Agent
- Career Agent
- Learning Roadmap Agent

### 5. Report Generation
The outputs from all agents are combined into a comprehensive final report using an LLM.

### 6. User Interface
The Streamlit application displays:
- ATS Analysis
- Skills Assessment
- Suggested Projects
- Career Recommendations
- Learning Roadmap
- Final Report
- Job Description Match
- Downloadable PDF Report