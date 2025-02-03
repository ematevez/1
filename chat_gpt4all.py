from gpt4all import GPT4All
import streamlit as st

# Cargar un modelo más pequeño como Mistral-7B o TinyLlama
model = GPT4All("mistral-7B.Q4_0.gguf")  # O prueba con TinyLlama

st.title("🤖 Chat con GPT4All (Optimizado para Streamlit Cloud)")

# Historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generar respuesta con GPT4All
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            with model.chat_session():
                response = model.generate(user_input)
            st.markdown(response)

    # Guardar la respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": response})
