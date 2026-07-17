"""
agent.py

Contains specialized AI agents for
resume analysis.
"""

from llm import call_llm

from prompts import (
    ATS_PROMPT,
    SKILLS_PROMPT,
    PROJECTS_PROMPT,
    CAREER_PROMPT,
    ROADMAP_PROMPT
)


def ats_agent(resume_text, context):
    """
    Performs ATS analysis.
    """

    prompt = ATS_PROMPT.format(
        resume_text=resume_text,
        context=context
    )

    return call_llm(
        prompt,
        system_prompt="You are an ATS resume evaluation expert."
    )


def skills_agent(resume_text, context):
    """
    Performs skills analysis.
    """

    prompt = SKILLS_PROMPT.format(
        resume_text=resume_text,
        context=context
    )

    return call_llm(
        prompt,
        system_prompt="You are a senior technical recruiter."
    )


def projects_agent(resume_text, context):
    """
    Suggests resume-strengthening projects.
    """

    prompt = PROJECTS_PROMPT.format(
        resume_text=resume_text,
        context=context
    )

    return call_llm(
        prompt,
        system_prompt="You are an engineering mentor."
    )


def career_agent(resume_text, context):
    """
    Suggests suitable career paths.
    """

    prompt = CAREER_PROMPT.format(
        resume_text=resume_text,
        context=context
    )

    return call_llm(
        prompt,
        system_prompt="You are an experienced career advisor."
    )


def roadmap_agent(resume_text, context):
    """
    Creates a personalized learning roadmap.
    """

    prompt = ROADMAP_PROMPT.format(
        resume_text=resume_text,
        context=context
    )

    return call_llm(
        prompt,
        system_prompt="You are a technical mentor."
    )