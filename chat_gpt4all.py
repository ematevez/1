import streamlit as st
import requests

# Configurar API de Hugging Face
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct"
HEADERS = {"Authorization": "Bearer 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"}  # Reemplaza con tu API Key de Hugging Face

st.title("🤖 Chat con Hugging Face")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": user_input})

            try:
                reply = response.json()[0]["generated_text"]
            except KeyError:
                reply = "❌ Error: No se encontró una respuesta válida."

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
