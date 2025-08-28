import google.genai as genai
from config import GEMINI_API_KEY, GPT_MAX_TOKENS

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_verification_questions(article_text: str) -> list:
    prompt = (
        "Generate 3-4 specific questions a reader should ask to independently verify the claims "
        "and content of the following news article. Return them as a numbered list in plain text.\n\n"
        f"Article:\n{article_text}\n\nVerification Questions:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    questions_text = response.text.strip()
    
    questions = []
    for line in questions_text.split('\n'):
        line = line.strip().lstrip("0123456789.-) ")
        if line:
            questions.append(line)
    
    if not questions:
        return ["Could not generate verification questions automatically."]
    
    return questions