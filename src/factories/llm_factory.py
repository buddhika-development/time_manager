from src.llm_models.gemini_llm import GEMINIConnection
from src.llm_models.mistral_llm import MistralConnection

class LLMFactory:

    _connections = {
        "gemini" : GEMINIConnection,
        "mistral" : MistralConnection
    }

    @classmethod
    def create(cls, llm_type:str, **kwargs):
        if llm_type.lower() not in cls._connections:
            raise ValueError(f"Invalid LLM type: {llm_type}")

        llm = cls._connections[llm_type.lower()](**kwargs)
        llm.connect()
        return llm