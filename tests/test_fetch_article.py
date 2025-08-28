from utils.fetch_article import fetch_article_text

def test_fetch_article_text():
    text = fetch_article_text("https://www.example.com")
    assert isinstance(text, str)
    assert "Example Domain" in text