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

# Limit the number of entities per category to keep the report concise
MAX_ENTITIES_PER_CATEGORY = 5

def generate_report(url: str, report_filename: str):
    """
    Generates a full critical analysis report for a given news article URL.
    The report includes:
    - Core claims
    - Language & tone analysis
    - Potential red flags
    - Verification questions
    - Entities & investigation prompts
    - Counter-argument simulation
    """
    
    # Step 1: Fetch the article text
    print("Fetching and processing article...")
    article_text = fetch_article_text(url)
    if not article_text:
        print("Error: Could not fetch article content.")
        return

    # Step 2: Clean the article text
    clean_article = clean_text(article_text)
    
    # Step 3: Extract core claims from the article
    print("Extracting core claims...")
    claims = extract_core_claims(clean_article)
    
    # Step 4: Analyze language and tone
    print("Analyzing language & tone...")
    tone_analysis = analyze_tone(clean_article)
    
    # Step 5: Detect potential red flags or biases
    print("Detecting potential red flags...")
    red_flags = detect_red_flags(clean_article)
    
    # Step 6: Generate verification questions for independent fact-checking
    print("Generating verification questions...")
    questions = generate_verification_questions(clean_article)
    
    # Step 7: Extract entities (people, organizations, locations) and generate investigation prompts
    print("Extracting entities & generating investigation prompts...")
    entities = extract_entities(clean_article)
    entity_prompts = generate_entity_prompts(entities)
    
    # Filter the entity prompts to only include a limited number per category for clarity
    filtered_prompts = []
    for category in ["PERSON", "ORG", "GPE"]:
        filtered = [p for p in entity_prompts if category in p][:MAX_ENTITIES_PER_CATEGORY]
        filtered_prompts.extend(filtered)
    
    # Step 8: Generate a counter-argument summary highlighting potential biases or alternate viewpoints
    print("Simulating counter-argument...")
    counter_argument = simulate_counter_argument(clean_article)
    
    # Step 9: Build the Markdown report
    report_lines = [
        f"# Critical Analysis Report for: {url}\n",
        "### Core Claims"
    ]
    for claim in claims:
        report_lines.append(f"* {claim}")
    
    # Add language and tone analysis section
    report_lines.extend([
        "\n### Language & Tone Analysis",
        f"**Classification:** {tone_analysis['classification']}",
        f"\n**Explanation:**\n{tone_analysis['explanation']}"
    ])
    
    # Add potential red flags section
    report_lines.append("\n### Potential Red Flags")
    for flag in red_flags:
        report_lines.append(f"* {flag}")
    
    # Add verification questions section
    report_lines.append("\n### Verification Questions")
    for q in questions:
        report_lines.append(f"1. {q}")
    
    # Add filtered entity prompts section if available
    if filtered_prompts:
        report_lines.append("\n### Entities & Investigation Prompts")
        for ep in filtered_prompts:
            report_lines.append(f"* {ep}")
    
    # Add counter-argument simulation section
    report_lines.append("\n### Counter-Argument Simulation")
    report_lines.append(counter_argument)
    
    # Combine all lines into a single string
    report_content = "\n".join(report_lines)
    
    # Step 10: Save the report to the reports directory
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
    
    report_path = os.path.join(REPORTS_DIR, report_filename)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"Report saved to: {report_path}")


# Entry point of the script
if __name__ == "__main__":
    url = input("Enter the article URL: ").strip()
    report_file = "analysis_report.md"
    generate_report(url, report_file)