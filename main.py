import os
from utils.fetch_article import fetch_article_text
from utils.text_processing import clean_text
from utils.claim_extraction import extract_core_claims
from utils.tone_analysis import analyze_tone
from utils.red_flags import detect_red_flags
from utils.verification_questions import generate_verification_questions
from config import REPORTS_DIR

def generate_report(url: str, report_filename: str):
    # Step 1: Fetch article
    print("Fetching article...")
    article_text = fetch_article_text(url)
    
    if not article_text:
        print("Failed to fetch article content.")
        return
    
    # Step 2: Clean article
    clean_article = clean_text(article_text)
    
    # Step 3: Extract core claims
    print("Extracting core claims...")
    claims = extract_core_claims(clean_article)
    
    # Step 4: Analyze tone
    print("Analyzing language and tone...")
    tone_analysis = analyze_tone(clean_article)
    
    # Step 5: Detect red flags
    print("Detecting potential red flags...")
    red_flags = detect_red_flags(clean_article)
    
    # Step 6: Generate verification questions
    print("Generating verification questions...")
    questions = generate_verification_questions(clean_article)
    
    # Step 7: Prepare report content
    report_lines = [
        f"# Critical Analysis Report for: {url}\n",
        "### Core Claims"
    ]
    for claim in claims:
        report_lines.append(f"* {claim}")
    
    report_lines.extend([
        "\n### Language & Tone Analysis",
        tone_analysis,
        "\n### Potential Red Flags"
    ])
    for flag in red_flags:
        report_lines.append(f"* {flag}")
    
    report_lines.extend([
        "\n### Verification Questions"
    ])
    for q in questions:
        report_lines.append(f"1. {q}")
    
    report_content = "\n".join(report_lines)
    
    # Step 8: Save report
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
    
    report_path = os.path.join(REPORTS_DIR, report_filename)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"Report saved to: {report_path}")

if __name__ == "__main__":
    url = input("Enter the article URL: ").strip()
    report_file = "analysis_report.md"
    generate_report(url, report_file)