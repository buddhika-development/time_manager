import os
from langchain_mistralai import ChatMistralAI
from src.llm_models.llm import LLMConnection


class MistralConnection(LLMConnection):
    def __init__(self):
        super().__init__()
        self.connect()
    
    def connect(self):
        self.llm = ChatMistralAI(
            model= "mistral-large-2512",
            mistral_api_key = os.getenv("MISTRAL_API_KEY"),
        )
    
    def invoke(self, message):
        return self.llm.invoke(message)
