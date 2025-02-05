import streamlit as st
import google.generativeai as genai


# Crear el modelo
def generar_cuento(caracteristica1, caracteristica2, caracteristica3, caracteristica4):
    # Configurar la API de Google Gemini
    API_KEY = "AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"Genera un cuento con las siguientes características:\n"
        f"1. {caracteristica1}\n"
        f"2. {caracteristica2}\n"
        f"3. {caracteristica3}\n"
        f"4. {caracteristica4}\n"
    )
    response = model.generate_content(prompt)
    return response.text

# Interfaz con Streamlit
st.title("Generador de Cuentos con IA ✨📖")

# Inputs para las características
desc1 = st.text_input("Característica 1")
desc2 = st.text_input("Característica 2")
desc3 = st.text_input("Característica 3")
desc4 = st.text_input("Característica 4")

if st.button("Generar Cuento 📝"):
    if desc1 and desc2 and desc3 and desc4:
        cuento = generar_cuento(desc1, desc2, desc3, desc4)
        st.subheader("Aquí está tu cuento:")
        st.write(cuento)
    else:
        st.warning("Por favor, completa las 4 características antes de generar el cuento.")
