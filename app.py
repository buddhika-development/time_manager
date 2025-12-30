import streamlit as st
from src.factories.llm_factory import LLMFactory

initial_chat_message = [
    {
        "role" : "assistant",
        "content" : "How can I help you to manage your time ?"
    }
]

llm = LLMFactory.create("gemini")

def session_state_init():
    if  "message_history" not in st.session_state:
        st.session_state.message_history = initial_chat_message

def main():
    session_state_init()

    # display the initial message
    for message in st.session_state.message_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if user_input := st.chat_input("Ask a question about time management"):
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.message_history.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            with st.spinner("Thinking..."):
                for chunk in llm.stream(user_input):
                    if hasattr(chunk, 'content'):
                        full_response += chunk.content
                        message_placeholder.write(full_response)
                    else:
                        full_response = str(chunk)
            st.session_state.message_history.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()