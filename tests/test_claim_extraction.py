from utils.claim_extraction import extract_core_claims

def test_extract_core_claims_returns_list():
    article_text = "Some dummy text to simulate an article."
    claims = extract_core_claims(article_text)
    assert isinstance(claims, list)
    assert len(claims) >= 1