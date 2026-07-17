"""
app.py

Main Streamlit application
for the AI Resume Analyzer.
"""

import os
import streamlit as st

from extracter import extract_text_from_pdf
from workflow import run_resume_workflow
from report_generator import create_pdf_report
from jd_matcher import analyze_job_match

# -----------------------------------------
# Streamlit Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# -----------------------------------------
# Title
# -----------------------------------------

st.title("📄 AI Resume Analyzer")

st.markdown("""
Upload your **Resume (PDF)** to receive the following insights:

- ✅ ATS Analysis
- ✅ Skills Assessment
- ✅ Recommended Projects
- ✅ Career Suggestions
- ✅ Learning Roadmap
- ✅ AI Generated Final Report
- ✅ Job Description Matching
- ✅ Downloadable PDF Report
""")

# -----------------------------------------
# Upload Resume
# -----------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------------------
# Process Uploaded Resume
# -----------------------------------------

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Resume uploaded successfully!")

    # -----------------------------------------
    # Extract Resume Text
    # -----------------------------------------

    try:

        resume_text = extract_text_from_pdf(file_path)

        st.subheader("📄 Extracted Resume")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

    except Exception as e:

        st.error(f"Error extracting resume:\n{e}")
        st.stop()

    # -----------------------------------------
    # Optional Job Description
    # -----------------------------------------

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the Job Description here",
        height=200,
        placeholder="Paste a job description to compare your resume..."
    )

    # -----------------------------------------
    # Analyze Button
    # -----------------------------------------

    if st.button("🚀 Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            try:

                results = run_resume_workflow(
                    resume_text
                )

            except Exception as e:

                st.error(f"Workflow Error:\n{e}")
                st.stop()

        st.success("✅ Analysis Complete!")

        # -----------------------------------------
        # Final Report
        # -----------------------------------------

        st.success("✅ Analysis Complete!")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 ATS",
            "🛠 Skills",
            "🚀 Projects",
            "💼 Career",
            "📚 Roadmap",
            "📋 Final Report"
        ])

        with tab1:
            st.markdown(results["ats"])

        with tab2:
            st.markdown(results["skills"])

        with tab3:
            st.markdown(results["projects"])

        with tab4:
            st.markdown(results["career"])

        with tab5:
            st.markdown(results["roadmap"])

        with tab6:
            st.markdown(results["final_report"])

        # -----------------------------------------
        # PDF Download
        # -----------------------------------------

        pdf_path = create_pdf_report(results)

        with open(pdf_path, "rb") as pdf:

            st.download_button(
                label="📥 Download Analysis Report",
                data=pdf,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

        # -----------------------------------------
        # Job Description Matching
        # -----------------------------------------

        if job_description.strip():

            st.divider()

            st.header("🎯 Job Description Match")

            with st.spinner("Comparing Resume with Job Description..."):

                jd_report = analyze_job_match(
                    resume_text,
                    job_description
                )

            st.markdown(jd_report)