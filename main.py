from utils.fetch_article import fetch_article_text
from utils.text_processing import clean_text
from utils.claim_extraction import extract_core_claims
from utils.tone_analysis import analyze_tone
from utils.red_flags import detect_red_flags
from utils.verification_questions import generate_verification_questions
from config import REPORTS_DIR
import os

def generate_report(url: str, output_file: str):
    article_text = fetch_article_text(url)
    if not article_text:
        print("Failed to fetch article.")
        return

    clean_article = clean_text(article_text)
    claims = extract_core_claims(clean_article)
    tone = analyze_tone(clean_article)
    red_flags = detect_red_flags(clean_article)
    questions = generate_verification_questions(claims)

    report_md = f"# Critical Analysis Report for: {url}\n\n"
    report_md += "### Core Claims\n" + "".join(f"* {c}\n" for c in claims) + "\n"
    report_md += "### Language & Tone Analysis\n" + tone + "\n\n"
    report_md += "### Potential Red Flags\n" + "".join(f"* {r}\n" for r in red_flags) + "\n"
    report_md += "### Verification Questions\n" + "".join(f"{i+1}. {q}\n" for i,q in enumerate(questions)) + "\n"

    os.makedirs(REPORTS_DIR, exist_ok=True)
    with open(os.path.join(REPORTS_DIR, output_file), "w") as f:
        f.write(report_md)

    print(f"Report saved to {REPORTS_DIR}/{output_file}")

if __name__ == "__main__":
    url = input("Enter the article URL: ").strip()
    generate_report(url, "analysis_report.md")
