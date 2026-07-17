"""
report_generator.py

Creates a professional PDF report
for the AI Resume Analyzer.
"""

import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(results):
    """
    Creates a PDF from workflow results.

    Parameters:
        results (dict): Output from run_resume_workflow()

    Returns:
        str: Path to generated PDF
    """

    os.makedirs("reports", exist_ok=True)

    pdf_path = "reports/Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    title = styles["Title"]
    heading = styles["Heading1"]
    body = styles["BodyText"]

    story = []

    # ----------------------------
    # Title
    # ----------------------------

    story.append(
        Paragraph(
            "AI Resume Analysis Report",
            title
        )
    )

    story.append(
        Paragraph(
            "Generated using LLM + RAG + Multi-Agent Workflow",
            body
        )
    )

    story.append(Spacer(1, 20))

    # ----------------------------
    # Helper Function
    # ----------------------------

    def add_section(title_text, content):

        story.append(
            Paragraph(title_text, heading)
        )

        story.append(Spacer(1, 6))

        for line in content.split("\n"):

            line = line.strip()

            if line:

                story.append(
                    Paragraph(line, body)
                )

        story.append(Spacer(1, 15))

    # ----------------------------
    # Sections
    # ----------------------------

    add_section(
        "ATS Analysis",
        results["ats"]
    )

    add_section(
        "Skills Analysis",
        results["skills"]
    )

    add_section(
        "Suggested Projects",
        results["projects"]
    )

    add_section(
        "Career Recommendations",
        results["career"]
    )

    add_section(
        "Learning Roadmap",
        results["roadmap"]
    )

    add_section(
        "Final Resume Report",
        results["final_report"]
    )

    doc.build(story)

    return pdf_path
