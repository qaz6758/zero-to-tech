import os

from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("AI_BASE_URL"),
)