import os
import streamlit as st
from gpt4all import GPT4All

# Cargar el modelo local de GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Configurar la interfaz en Streamlit
st.title("🤖 BabyAGI con GPT4All para Subir Archivos a Streamlit")

uploaded_file = st.file_uploader("Sube tu archivo aquí:")
if uploaded_file:
    # Guardar el archivo en la carpeta "uploads"
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded_file.name)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ Archivo {uploaded_file.name} subido con éxito.")

    # Crear una tarea para que el agente analice la subida del archivo
    task = f"El usuario ha subido un archivo llamado {uploaded_file.name}. ¿Qué debería hacer con él?"

    # Ejecutar GPT4All localmente
    with model.chat_session():
        response = model.generate(task)

    # Mostrar el resultado del agente
    st.write("🤖 Respuesta del Agente:")
    st.write(response)
