import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def simulate_counter_argument(article_text: str) -> str:
    """
    Generates a concise opposing viewpoint or counter-argument to highlight biases in the article.

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - str: Counter-argument text.
    """
    prompt = (
        "Summarize the article from a hypothetical opposing viewpoint. "
        "Highlight potential biases, assumptions, or alternative interpretations.\n\n"
        f"Article:\n{article_text}\n\nCounter-Argument:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text.strip() if response.text.strip() else "Could not generate counter-argument automatically."