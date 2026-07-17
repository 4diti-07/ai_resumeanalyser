"""
jd_matcher.py

Compares a resume with a job description
using the LLM.
"""

from llm import call_llm


def analyze_job_match(resume_text, job_description):
    """
    Compare a resume against a job description.

    Args:
        resume_text (str): Resume text.
        job_description (str): Job description.

    Returns:
        str: AI-generated comparison report.
    """

    prompt = f"""
You are an experienced ATS recruiter and hiring manager.

Compare the following resume with the job description.

=========================
RESUME
=========================

{resume_text}

=========================
JOB DESCRIPTION
=========================

{job_description}

Generate a professional report in Markdown.

Include the following sections:

# ATS Match Score
(Give a score out of 100)

# Matching Skills

# Missing Skills

# Missing Keywords

# Candidate Strengths

# Candidate Weaknesses

# Resume Improvements

# Final Recommendation

Be specific and actionable.
"""

    return call_llm(
        prompt,
        system_prompt="You are an expert technical recruiter."
    )