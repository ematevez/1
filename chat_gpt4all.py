#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
import streamlit as st
import requests

# Título de la app
st.title("🤖 Chat con OpenRouter (So)")

# URL de la API de OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"
# Asegúrate de que tu API Key esté correcta
#HEADERS = {"Authorization": "Bearer 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"}
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Historial de la conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar el historial de mensajes
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Solicitar entrada del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Agregar el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(user_input)

    # Llamada a la API para obtener la respuesta del modelo
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = requests.post(API_URL, json={
                "model": "openai/gpt-3.5-turbo",  # Modelo seleccionado
                "messages": st.session_state.messages
            }, headers=HEADERS)

            # 📌 Imprime la respuesta completa para depurar
            st.write("🔍 Respuesta JSON:", response.json())

            # Intentar obtener la respuesta del modelo
            try:
                reply = response.json()["choices"][0]["message"]["content"]
            except KeyError:
                reply = "❌ Error: No se encontró una respuesta válida en la API."

            # Mostrar la respuesta del asistente
            st.markdown(reply)

    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": reply})
