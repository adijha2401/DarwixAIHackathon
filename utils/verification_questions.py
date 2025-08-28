import google.genai as genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_verification_questions(article_text: str) -> list:
    """
    Generates 3-4 specific verification questions for readers to fact-check the article.

    Parameters:
    - article_text (str): Cleaned article text.

    Returns:
    - list: List of questions.
    """
    prompt = (
        "Generate 3-4 specific questions a reader should ask to verify the factual accuracy "
        "and credibility of this news article.\n\n"
        f"Article:\n{article_text}\n\nVerification Questions:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    text = response.text.strip()
    questions = [line.strip("1234567890.-* ") for line in text.split("\n") if line.strip()]
    return questions if questions else ["Could not generate verification questions automatically."]