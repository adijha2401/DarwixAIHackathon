import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str) -> str:
    """
    Fetches the main text content of a news article from a given URL.

    Parameters:
    - url (str): The URL of the news article.

    Returns:
    - str: The cleaned text content of the article.
           Returns an empty string if fetching fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the article: {e}")
        return ""
    
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract text from <p> tags (main content)
    paragraphs = soup.find_all("p")
    article_text = "\n".join([p.get_text() for p in paragraphs])
    
    return article_text