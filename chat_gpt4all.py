import streamlit as st
import requests

st.title("🤖 Chat con OpenRouter (Gratis)")

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {"Authorization": "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"}

# Historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = requests.post(API_URL, json={
                "model": "mistralai/mistral-7b-instruct",
                "messages": st.session_state.messages
            }, headers=HEADERS)

            reply = response.json()["choices"][0]["message"]["content"]
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

