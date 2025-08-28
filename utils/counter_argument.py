import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def simulate_counter_argument(article_text: str) -> str:
    prompt = (
        "Summarize the following article from a hypothetical opposing viewpoint. "
        "Highlight alternative interpretations or critiques of the claims made.\n\n"
        f"Article:\n{article_text}\n\nCounter-Argument Summary:"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text.strip()