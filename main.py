import os
from config import REPORTS_DIR
from utils.fetch_article import fetch_article_text
from utils.text_processing import clean_text
from utils.claim_extraction import extract_core_claims
from utils.tone_analysis import analyze_tone
from utils.red_flags import detect_red_flags
from utils.verification_questions import generate_verification_questions
from utils.entity_analysis import extract_entities, generate_entity_prompts
from utils.counter_argument import simulate_counter_argument

MAX_ENTITIES_PER_CATEGORY = 5  # Limit to keep report clean

def generate_report(url: str, report_filename: str = None):
    """
    Fetches an article, analyzes it, and generates a critical analysis report.
    If report_filename is provided, saves it to the reports folder.
    Returns the report content as a string.
    """
    print("Fetching and processing article...")
    article_text = fetch_article_text(url)
    if not article_text:
        print("Error: Could not fetch article content.")
        return "Error: Could not fetch article content."
    clean_article = clean_text(article_text)

    print("Extracting core claims...")
    claims = extract_core_claims(clean_article)

    print("Analyzing language & tone...")
    tone_analysis = analyze_tone(clean_article)

    print("Detecting potential red flags...")
    red_flags = detect_red_flags(clean_article)

    print("Generating verification questions...")
    questions = generate_verification_questions(clean_article)

    print("Extracting entities & generating investigation prompts...")
    entities = extract_entities(clean_article)
    entity_prompts = generate_entity_prompts(entities)

    # Limit number of entities for clarity
    filtered_prompts = []
    for category in ["PERSON", "ORG", "GPE"]:
        filtered = [p for p in entity_prompts if category in p][:MAX_ENTITIES_PER_CATEGORY]
        filtered_prompts.extend(filtered)

    print("Simulating counter-argument...")
    counter_argument = simulate_counter_argument(clean_article)

    # Build report as a string
    report_lines = [f"# Critical Analysis Report for: {url}\n"]

    report_lines.append("### Core Claims")
    if claims:
        for claim in claims:
            report_lines.append(f"* {claim}")
    else:
        report_lines.append("* Could not extract claims automatically.")

    report_lines.append("\n### Language & Tone Analysis")
    report_lines.append(f"**Classification:** {tone_analysis.get('classification', 'N/A')}")
    report_lines.append(f"**Explanation:**\n{tone_analysis.get('explanation', 'N/A')}")

    report_lines.append("\n### Potential Red Flags")
    if red_flags:
        for flag in red_flags:
            report_lines.append(f"* {flag}")
    else:
        report_lines.append("* Could not detect red flags automatically.")

    report_lines.append("\n### Verification Questions")
    if questions:
        for idx, q in enumerate(questions, 1):
            report_lines.append(f"{idx}. {q}")
    else:
        report_lines.append("* Could not generate verification questions automatically.")

    if filtered_prompts:
        report_lines.append("\n### Entities & Investigation Prompts")
        for ep in filtered_prompts:
            report_lines.append(f"* {ep}")

    report_lines.append("\n### Counter-Argument Simulation")
    report_lines.append(counter_argument if counter_argument else "* Could not generate counter-argument automatically.")

    report_content = "\n".join(report_lines)

    # Save to file if filename is provided
    if report_filename:
        if not os.path.exists(REPORTS_DIR):
            os.makedirs(REPORTS_DIR)
        report_path = os.path.join(REPORTS_DIR, report_filename)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"Report saved to: {report_path}")

    return report_content


if __name__ == "__main__":
    url = input("Enter the article URL: ").strip()
    report_file = "analysis_report.md"
    report_content = generate_report(url, report_file)
    print("\nReport Generated:\n")
    print(report_content)