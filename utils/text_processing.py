import re

def clean_text(text: str) -> str:
    """
    Cleans article text by removing extra spaces, newlines, and unwanted characters.

    Parameters:
    - text (str): Raw article text.

    Returns:
    - str: Cleaned text.
    """
    # Remove multiple newlines and replace with single newline
    text = re.sub(r'\n+', '\n', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing spaces
    text = text.strip()
    return text