import os
from dotenv import load_dotenv

load_dotenv()

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
REQUEST_TIMEOUT = 10

REPORTS_DIR = "reports/"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GPT_MAX_TOKENS = 300