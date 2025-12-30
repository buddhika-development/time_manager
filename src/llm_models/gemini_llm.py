from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from src.llm_models.llm import LLMConnection

load_dotenv()

class GEMINIConnection(LLMConnection):
    def __init__(self):
        super().__init__()
        self.connect()
    
    def connect(self):
        self.llm = ChatGoogleGenerativeAI(
            model= "models/gemini-2.5-flash",
            google_api_key = os.getenv("GOOGLE_API_KEY"),
        )
    
    def invoke(self, message):
        return self.llm.invoke(message)
