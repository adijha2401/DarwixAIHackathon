from utils.tone_analysis import analyze_tone

def test_analyze_tone_returns_string():
    article_text = "Some dummy text to simulate an article."
    tone = analyze_tone(article_text)
    assert isinstance(tone, str)
    assert len(tone) > 0