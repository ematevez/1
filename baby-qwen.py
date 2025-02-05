import streamlit as st
import google.generativeai as genai
import threading
import time

# Configuración inicial de la API de Google Gemini
API_KEY = "AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Función para generar un cuento
def generar_cuento(caracteristica1, caracteristica2, caracteristica3, caracteristica4):
    prompt = (
        f"Genera un cuento con las siguientes características:\n"
        f"1. {caracteristica1}\n"
        f"2. {caracteristica2}\n"
        f"3. {caracteristica3}\n"
        f"4. {caracteristica4}\n"
    )
    response = model.generate_content(prompt)
    return response.text

# Variables globales para almacenar el estado del cuento
cuento_generado = ""
generando_cuento = False

# Función de automatización continua
def automatizacion_continua():
    global cuento_generado, generando_cuento
    while True:
        if generando_cuento:
            # Características predefinidas para automatización
            caracteristicas = [
                "Un héroe valiente",
                "Un reino mágico",
                "Un dragón malvado",
                "Un tesoro escondido"
            ]
            cuento_generado = generar_cuento(*caracteristicas)
            generando_cuento = False  # Detener la generación después de completar
        time.sleep(5)  # Esperar antes de la próxima iteración

# Iniciar el hilo de automatización en segundo plano
thread = threading.Thread(target=automatizacion_continua, daemon=True)
thread.start()

# Interfaz con Streamlit
st.title("Generador de Cuentos con IA ✨📖")

# Inputs para las características
desc1 = st.text_input("Característica 1")
desc2 = st.text_input("Característica 2")
desc3 = st.text_input("Característica 3")
desc4 = st.text_input("Característica 4")

# Botón para generar un cuento manualmente
if st.button("Generar Cuento Manual 📝"):
    if desc1 and desc2 and desc3 and desc4:
        cuento_generado = generar_cuento(desc1, desc2, desc3, desc4)
        st.subheader("Aquí está tu cuento:")
        st.write(cuento_generado)
    else:
        st.warning("Por favor, completa las 4 características antes de generar el cuento.")

# Botón para iniciar/parar la generación automática
if st.button("Iniciar/Pausar Generación Automática ⏯️"):
    generando_cuento = not generando_cuento
    if generando_cuento:
        st.info("Generación automática iniciada. ¡Espera tu cuento!")
    else:
        st.info("Generación automática pausada.")

# Mostrar el último cuento generado automáticamente
if cuento_generado:
    st.subheader("Último cuento generado automáticamente:")
    st.write(cuento_generado)