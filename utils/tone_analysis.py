import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_tone(article_text: str) -> str:
    prompt = (
        "Analyze the following news article and describe its language and tone. "
        "Classify it as 'Neutral', 'Persuasive', 'Opinionated', or 'Emotionally Charged', "
        "and give a short explanation.\n\n"
        f"Article:\n{article_text}\n\nTone Analysis:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()
