from utils.text_processing import clean_text

def test_clean_text_basic():
    raw = " This is   a \n test  "
    cleaned = clean_text(raw)
    assert cleaned == "This is a test"

def test_clean_text_empty():
    raw = "   \n  "
    cleaned = clean_text(raw)
    assert cleaned == ""