import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model="gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)