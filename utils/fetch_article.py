import requests
from bs4 import BeautifulSoup
from config import USER_AGENT

def fetch_article_text(url: str) -> str:
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text() for p in paragraphs)
    except Exception as e:
        print(f"Error fetching article: {e}")
        return ""