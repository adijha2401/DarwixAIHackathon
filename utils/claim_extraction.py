import google.genai as genai
from config import GEMINI_API_KEY, GPT_MAX_TOKENS

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_core_claims(article_text: str) -> list:
    prompt = (
        "Read the following news article and extract 3-5 core factual claims. "
        "Return them as a numbered list in plain text (do NOT use Python list format).\n\n"
        f"Article:\n{article_text}\n\nClaims:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    claims_text = response.text.strip()
    
    claims = []
    for line in claims_text.split('\n'):
        line = line.strip()
        if line:
            line = line.lstrip("0123456789.-) ")
            claims.append(line)
    
    if not claims:
        return ["Could not extract claims automatically."]
    
    return claims