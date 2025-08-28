import google.genai as genai
from config import GEMINI_API_KEY, GPT_MAX_TOKENS

client = genai.Client(api_key=GEMINI_API_KEY)

def detect_red_flags(article_text: str) -> list:
    prompt = (
        "Analyze the following news article for potential red flags or bias. "
        "Return a bulleted list in plain text of any issues like loaded language, "
        "lack of sources, dismissing opposing views, or over-reliance on anonymous sources.\n\n"
        f"Article:\n{article_text}\n\nRed Flags:"
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    
    flags_text = response.text.strip()
    
    flags = []
    for line in flags_text.split('\n'):
        line = line.strip().lstrip("*-• ")
        if line:
            flags.append(line)
    
    if not flags:
        return ["Could not detect red flags automatically."]
    
    return flags