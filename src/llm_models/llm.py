from abc import ABC, abstractmethod

class LLMConnection(ABC):
    def __init__(self):
        self.llm = None
    
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def invoke(self, message):
        pass