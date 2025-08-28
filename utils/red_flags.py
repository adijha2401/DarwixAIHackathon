import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def detect_red_flags(article_text: str) -> list:
    prompt = (
        "Read the following article and identify potential red flags, such as bias, "
        "loaded language, over-reliance on anonymous sources, or missing data. "
        "Return a Python list of bullet points.\n\n"
        f"Article:\n{article_text}\n\nRed Flags:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=150
    )
    flags_text = response['choices'][0]['message']['content']
    try:
        flags_list = eval(flags_text)
        if isinstance(flags_list, list):
            return flags_list
    except:
        pass
    return ["Could not detect red flags automatically."]
