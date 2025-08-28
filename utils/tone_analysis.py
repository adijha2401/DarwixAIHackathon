import google.genai as genai
from config import GEMINI_API_KEY, GPT_MAX_TOKENS

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_tone(article_text: str) -> str:
    prompt = (
        "Analyze the following news article and describe its language and tone. "
        "Classify it as 'Neutral', 'Persuasive', 'Opinionated', or 'Emotionally Charged', "
        "and give a short explanation.\n\n"
        f"Article:\n{article_text}\n\nTone Analysis:"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    tone = response.text.strip()
    
    return tone