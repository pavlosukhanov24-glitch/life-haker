import streamlit as st

st.set_page_config(page_title="Life Hacks Bot 🤖")

st.title("🧠 Life Hacks Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask me for a life hack...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Simple placeholder response
    response = f"Here’s a life hack for you: Stay curious about '{prompt}' 😉"

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)
