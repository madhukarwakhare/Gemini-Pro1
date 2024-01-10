from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
print(os.getenv("GOOGLE_API_KEY"))


llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke("Write a ballad about winter season")
print(result.content)