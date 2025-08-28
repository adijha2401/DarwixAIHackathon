from utils.red_flags import detect_red_flags

def test_detect_red_flags_returns_list():
    article_text = "Some dummy text to simulate an article."
    flags = detect_red_flags(article_text)
    assert isinstance(flags, list)
    assert len(flags) >= 1