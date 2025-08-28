import openai
from config import OPENAI_API_KEY, GPT_MAX_TOKENS

openai.api_key = OPENAI_API_KEY

def extract_core_claims(article_text: str) -> list:
    prompt = (
        "Read the following news article and extract 3-5 core factual claims. "
        "Return them as a Python list of strings.\n\n"
        f"Article:\n{article_text}\n\nClaims:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=GPT_MAX_TOKENS
    )
    claims_text = response['choices'][0]['message']['content']
    try:
        claims_list = eval(claims_text)
        if isinstance(claims_list, list):
            return claims_list
    except:
        pass
    return ["Could not extract claims automatically."]
