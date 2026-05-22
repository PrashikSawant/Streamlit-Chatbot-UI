import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    model = st.selectbox(
        "Choose Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
        ]
    )
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    st.caption("Day 10 — 30 Day AI Bootcamp")
    st.caption(f"Model: `{model}`")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # show user message
    with st.chat_message("user"):
        st.write(user_input)

    # add to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=model,
                messages=st.session_state.messages,
                max_tokens=1000,
                temperature=0.7
            )
            reply = response.choices[0].message.content
        st.write(reply)

    # add reply to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })