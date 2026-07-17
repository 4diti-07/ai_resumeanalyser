"""
workflow.py

Coordinates all AI agents using RAG.
"""

from rag import retrieve_context

from agent import (
    ats_agent,
    skills_agent,
    projects_agent,
    career_agent,
    roadmap_agent
)

from llm import call_llm


def run_resume_workflow(resume_text):

    # Retrieve relevant context from ChromaDB
    context = retrieve_context(resume_text)

    # Run all agents
    ats = ats_agent(resume_text, context)

    skills = skills_agent(resume_text, context)

    projects = projects_agent(resume_text, context)

    career = career_agent(resume_text, context)

    roadmap = roadmap_agent(resume_text, context)

    final_prompt = f"""
You are a senior technical recruiter.

Combine the following analyses into one professional report.

ATS Analysis:
{ats}

Skills Analysis:
{skills}

Projects Analysis:
{projects}

Career Advice:
{career}

Learning Roadmap:
{roadmap}

Create the final report using these sections:

# Overall Resume Score

# Strengths

# Weaknesses

# Missing Skills

# Suggested Projects

# Career Advice

# 3-Month Learning Roadmap

# Final Recommendations
"""

    final_report = call_llm(final_prompt)

    return {
        "ats": ats,
        "skills": skills,
        "projects": projects,
        "career": career,
        "roadmap": roadmap,
        "final_report": final_report
    }