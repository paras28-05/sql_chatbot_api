import os
from dotenv import load_dotenv
load_dotenv()
#langsmith_api_key = os.environ.get("LANGSMITH_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Local SQL Agent"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
#os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


#from langchain_ollama import ChatOllama

#llm = ChatOllama(model="llama3.1:8b")  #"llama3.1"

from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-1.5-flash")
