import streamlit as st
from gpt4all import GPT4All

# Cargar el modelo GPT4All
model_path = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"  # Asegúrate de que el archivo está en esta ubicación
model = GPT4All(model_path)

# Configurar la interfaz en Streamlit
st.title("🤖 Chat con GPT4All (Offline)")

# Inicializar el historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    # Guardar el mensaje del usuario
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
