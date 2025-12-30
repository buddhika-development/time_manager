"""
app.py provide the main interface of the application
"""

import streamlit as st
import sys
import os

# Ensure src is in python path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from chat_engine import ChatEngine

# Page Configuration
st.set_page_config(
    page_title="Time Manager",
    page_icon="🤖",
    layout="centered"
)

def initialize_session_state():
    """Initialize session state variables."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "message": "Hello! I am your AI assistant. How can I help you today?"
            }
        ]
    if "chat_engine" not in st.session_state:
        st.session_state.chat_engine = ChatEngine()

def main():
    initialize_session_state()
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["message"])

    # Chat Input
    if prompt := st.chat_input("Hi, how can I help you today?"):
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "message": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate response
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            # Stream the response
            for chunk in st.session_state.chat_engine.process_message(prompt, st.session_state.chat_history):
                full_response += chunk
                response_placeholder.write(full_response + "▌")
                
            response_placeholder.write(full_response)
            
        # Add assistant response to history
        st.session_state.chat_history.append({"role": "assistant", "message": full_response})

if __name__ == "__main__":
    main()
