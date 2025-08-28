import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_core_claims(article_text: str) -> list:
    """
    Uses Gemini AI to extract 3-5 main factual claims from the article.

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - list: A list of strings, each representing a core claim.
    """
    prompt = (
        "Extract 3-5 core factual claims from the following article.\n\n"
        f"Article:\n{article_text}\n\nCore Claims:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    # Parse the response: split by lines and remove empty entries
    text = response.text.strip()
    claims = [line.strip("-* ") for line in text.split("\n") if line.strip()]
    return claims if claims else ["Could not extract claims automatically."]