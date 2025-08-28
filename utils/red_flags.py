import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def detect_red_flags(article_text: str) -> list:
    """
    Identifies potential signs of bias, loaded language, or poor reporting.

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - list: List of detected red flags.
    """
    prompt = (
        "Identify potential red flags or biases in this news article. "
        "Include loaded terminology, over-reliance on anonymous sources, "
        "lack of cited data, or dismissed viewpoints.\n\n"
        f"Article:\n{article_text}\n\nRed Flags:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    text = response.text.strip()
    flags = [line.strip("-* ") for line in text.split("\n") if line.strip()]
    return flags if flags else ["Could not detect red flags automatically."]