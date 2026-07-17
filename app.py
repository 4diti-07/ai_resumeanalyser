import os
import streamlit as st

from extracter import extract_text_from_pdf
from workflow import run_resume_workflow
from jd_matcher import analyze_job_match
from report_generator import generate_pdf_report

#config

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

#handy sidebar

with st.sidebar:

    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.markdown("### Features")

    st.write("✅ ATS Resume Analysis")
    st.write("✅ Skill Gap Detection")
    st.write("✅ Project Recommendations")
    st.write("✅ Career Guidance")
    st.write("✅ Learning Roadmap")
    st.write("✅ Job Description Matching")
    st.write("✅ Download PDF Report")

    st.markdown("---")

    st.markdown("### Tech Stack")

    st.caption("• Streamlit")
    st.caption("• LangChain")
    st.caption("• ChromaDB")
    st.caption("• HuggingFace")
    st.caption("• OpenRouter GPT-4.1 Mini")

    st.markdown("---")

    st.caption("Built by Aditi Sharma")

#main title
st.title("📄 AI Resume Analyzer")

st.caption(
    "Analyze resumes using AI-powered ATS evaluation, "
    "RAG, LLMs, and personalized career recommendations."
)

st.divider()

#the upload section

left, right = st.columns(2)

with left:

    uploaded_resume = st.file_uploader(
        "📄 Upload Resume (PDF)",
        type=["pdf"]
    )

with right:

    uploaded_jd = st.file_uploader(
        "💼 Upload Job Description (Optional)",
        type=["pdf", "txt"]
    )

st.divider()

#to analyze the resume (button)

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

if analyze:

    if uploaded_resume is None:

        st.warning("Please upload a resume.")

        st.stop()

    os.makedirs("uploads", exist_ok=True)

    resume_path = os.path.join(
        "uploads",
        uploaded_resume.name
    )

    with open(resume_path, "wb") as f:
        f.write(uploaded_resume.getbuffer())

    progress = st.progress(0)

    with st.spinner("Extracting resume..."):

        resume_text = extract_text_from_pdf(
            resume_path
        )

    progress.progress(30)

    with st.expander("📄 Resume Preview"):

        st.text_area(
            "",
            resume_text,
            height=250
        )

    with st.spinner(
        "Analyzing your resume... This may take a few moments."
    ):

        report = run_resume_workflow(
            resume_text
        )

    progress.progress(80)

    st.success("✅ Resume analysis completed successfully!")

    st.divider()

    #ATS Analysis

    with st.expander("🎯 ATS Analysis", expanded=True):
        st.markdown(report["ats"])

    # skills analysis

    with st.expander("🛠 Skills Analysis"):
        st.markdown(report["skills"])

    #ai recommended projects tailored to the resume

    with st.expander("💡 Recommended Projects"):
        st.markdown(report["projects"])

    # career guidance based on the resume

    with st.expander("🚀 Career Guidance"):
        st.markdown(report["career"])

    # a suggested 30-day learning roadmap based on the resume

    with st.expander("📚 Learning Roadmap"):
        st.markdown(report["roadmap"])

    # the final report combining all the analyses into one professional report

    with st.expander("📋 Complete AI Report"):
        st.markdown(report["final_report"])

    progress.progress(90)

    # job description matching if a job description is uploaded
    if uploaded_jd is not None:

        st.divider()

        st.subheader("💼 Job Description Match")

        if uploaded_jd.name.endswith(".pdf"):

            jd_path = os.path.join(
                "uploads",
                uploaded_jd.name
            )

            with open(jd_path, "wb") as f:
                f.write(uploaded_jd.getbuffer())

            jd_text = extract_text_from_pdf(jd_path)

        else:

            jd_text = uploaded_jd.read().decode("utf-8")

        with st.spinner("Comparing resume with job description..."):

            jd_report = analyze_job_match(
                resume_text,
                jd_text
            )

        st.markdown(jd_report)

    progress.progress(100)
    progress.empty()

    # download the final report as a PDF

    st.divider()

    st.subheader("📥 Download Report")

    pdf_path = generate_pdf_report(report)

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

#final footer

st.divider()

st.caption(
    "🤖 AI Resume Analyzer • Powered by Streamlit, LangChain, ChromaDB, OpenRouter & Hugging Face"
)