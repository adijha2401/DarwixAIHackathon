import streamlit as st
from main import generate_report
from config import REPORTS_DIR

st.title("Digital Skeptic AI")
st.write("Empowering Critical Thinking in an Age of Information Overload")

url = st.text_input("Enter a news article URL:")

if st.button("Generate Report"):
    if not url:
        st.warning("Please enter a URL")
    else:
        report_filename = "analysis_report.md"
        generate_report(url, report_filename)
        st.success(f"Report saved in {REPORTS_DIR}/{report_filename}")
        with open(f"{REPORTS_DIR}/{report_filename}", "r", encoding="utf-8") as f:
            st.markdown(f.read())