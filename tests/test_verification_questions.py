from utils.verification_questions import generate_verification_questions

def test_generate_verification_questions_returns_list():
    claims = ["Claim 1", "Claim 2"]
    questions = generate_verification_questions(claims)
    assert isinstance(questions, list)
    assert len(questions) >= 1