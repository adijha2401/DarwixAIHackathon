import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_verification_questions(claims: list) -> list:
    claims_text = "\n".join(f"- {c}" for c in claims)
    prompt = (
        "Based on the following list of claims from a news article, generate 3-4 specific "
        "questions a reader should ask to independently verify the content. Return as a Python list.\n\n"
        f"Claims:\n{claims_text}\n\nVerification Questions:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=150
    )
    questions_text = response['choices'][0]['message']['content']
    try:
        questions_list = eval(questions_text)
        if isinstance(questions_list, list):
            return questions_list
    except:
        pass
    return ["Could not generate verification questions automatically."]