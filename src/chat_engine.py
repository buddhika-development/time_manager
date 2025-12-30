import time
from typing import Generator, List, Dict, Any

class ChatEngine:
    """
    Handles the chat logic and interaction with the LLM (mocked for now).
    """

    def __init__(self):
        pass

    def process_message(self, user_message: str, chat_history: List[Dict[str, Any]]) -> Generator[str, None, None]:
        """
        Process the user message and return a streaming response.
        
        Args:
            user_message (str): The input message from the user.
            chat_history (List[Dict]): Previous chat history.
            
        Yields:
            str: Chunks of the response.
        """
        # Simulate thinking or api processing time
        time.sleep(0.5)
        
        # Mock response logic
        response_template = f"Echo: {user_message}. (This is a mock response from ChatEngine)"
        
        # Simulate streaming
        for word in response_template.split():
            yield word + " "
            time.sleep(0.05)
