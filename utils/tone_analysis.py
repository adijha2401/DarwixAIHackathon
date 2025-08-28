import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_tone(article_text: str) -> dict:
    """
    Analyzes the language and tone of the article using Gemini AI.
    Classifies as 'Neutral', 'Persuasive', 'Opinionated', or 'Emotionally Charged'.

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - dict: {'classification': str, 'explanation': str}
    """
    prompt = (
        "Analyze the following article for language and tone. "
        "Classify as 'Neutral', 'Persuasive', 'Opinionated', or 'Emotionally Charged'. "
        "Provide a concise explanation without repeating labels.\n\n"
        f"Article:\n{article_text}\n\nTone Analysis:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    text = response.text.strip()
    
    # Parse response: first line = classification, rest = explanation
    lines = text.split("\n")
    classification = lines[0].replace("Classification:", "").strip() if lines else "Neutral"
    explanation = "\n".join(lines[1:]).replace("Explanation:", "").strip() if len(lines) > 1 else ""
    
    return {"classification": classification, "explanation": explanation}