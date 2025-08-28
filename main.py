import os
from utils.fetch_article import fetch_article_text
from utils.text_processing import clean_text
from utils.claim_extraction import extract_core_claims
from utils.tone_analysis import analyze_tone
from utils.red_flags import detect_red_flags
from utils.verification_questions import generate_verification_questions
from utils.entity_analysis import extract_entities, generate_entity_prompts
from utils.counter_argument import simulate_counter_argument
from config import REPORTS_DIR

def generate_report(url: str, report_filename: str):
    print("Fetching article...")
    article_text = fetch_article_text(url)
    
    if not article_text:
        print("Failed to fetch article content.")
        return
    
    clean_article = clean_text(article_text)
    
    print("Extracting core claims...")
    claims = extract_core_claims(clean_article)
    
    print("Analyzing language and tone...")
    tone_analysis = analyze_tone(clean_article)
    
    print("Detecting potential red flags...")
    red_flags = detect_red_flags(clean_article)
    
    print("Generating verification questions...")
    questions = generate_verification_questions(clean_article)
    
    print("Extracting entities and generating investigation prompts...")
    entities = extract_entities(clean_article)
    entity_prompts = generate_entity_prompts(entities)
    
    print("Generating counter-argument summary...")
    counter_argument = simulate_counter_argument(clean_article)
    
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
    
    report_lines.extend([
        "\n### Entities & Investigation Prompts"
    ])
    for ep in entity_prompts:
        report_lines.append(f"* {ep}")
    
    report_lines.extend([
        "\n### Counter-Argument Simulation",
        counter_argument
    ])
    
    report_content = "\n".join(report_lines)
    
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