import streamlit as st
import google.generativeai as genai

# Configurar la API de Google Gemini
API_KEY = ""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Función para generar respuestas
def generar_respuesta(prompt):
    response = model.generate_content(prompt)
    return response.text

# Interfaz en Streamlit
st.title("🤖 Asistente de Automatización con IA")
st.write("Selecciona una función y proporciona los datos necesarios.")

# Opciones de funciones
opciones = [
    "📅 Planificador de Tareas",
    "📖 Generador de Estrategias de Estudio",
    "🐞 Asistente de Resolución de Errores",
    "📚 Generador de Cuentos Interactivos",
    "💼 Generador de Respuestas para Clientes",
    "📱 Generador de Posts para Redes",
    "📝 Analizador de Opiniones",
    "👨‍🏫 Tutor Virtual de Programación",
    "🚀 Generador de Ideas para Startups"
]
eleccion = st.selectbox("Selecciona una función", opciones)

# Entrada de datos según la opción seleccionada
if eleccion == "📅 Planificador de Tareas":
    tareas = st.text_area("📌 Lista de tareas (separadas por comas)")
    if st.button("Generar Plan"):
        prompt = f"Organiza estas tareas de forma óptima: {tareas}"
        st.write(generar_respuesta(prompt))

elif eleccion == "📖 Generador de Estrategias de Estudio":
    tema = st.text_input("📘 Tema de estudio")
    dias = st.number_input("📅 Días disponibles", min_value=1, value=7)
    horas = st.number_input("⏳ Horas por día", min_value=1, value=2)
    if st.button("Generar Plan de Estudio"):
        prompt = f"Genera un plan de estudio de {tema} en {dias} días estudiando {horas} horas diarias."
        st.write(generar_respuesta(prompt))

elif eleccion == "🐞 Asistente de Resolución de Errores":
    error = st.text_area("⚠️ Ingresa el mensaje de error")
    if st.button("Solucionar Error"):
        prompt = f"Explica y soluciona este error de código: {error}"
        st.write(generar_respuesta(prompt))

elif eleccion == "📚 Generador de Cuentos Interactivos":
    descripcion = st.text_area("📝 Describe tu historia")
    if st.button("Generar Cuento"):
        prompt = f"Escribe un cuento basado en esta descripción: {descripcion}"
        st.write(generar_respuesta(prompt))

elif eleccion == "💼 Generador de Respuestas para Clientes":
    consulta = st.text_area("✉️ Ingresa la consulta del cliente")
    if st.button("Generar Respuesta"):
        prompt = f"Redacta una respuesta profesional a esta consulta: {consulta}"
        st.write(generar_respuesta(prompt))

elif eleccion == "📱 Generador de Posts para Redes":
    tema_post = st.text_input("📢 Tema del post")
    if st.button("Generar Post"):
        prompt = f"Genera un post atractivo para redes sociales sobre {tema_post}."
        st.write(generar_respuesta(prompt))

elif eleccion == "📝 Analizador de Opiniones":
    opinion = st.text_area("🗣️ Ingresa una opinión de cliente")
    if st.button("Analizar Opinión"):
        prompt = f"Analiza el sentimiento de esta opinión y genera una respuesta adecuada: {opinion}"
        st.write(generar_respuesta(prompt))

elif eleccion == "👨‍🏫 Tutor Virtual de Programación":
    tema_programacion = st.text_input("💻 Tema de programación")
    if st.button("Generar Guía"):
        prompt = f"Genera una guía paso a paso para aprender {tema_programacion} desde cero."
        st.write(generar_respuesta(prompt))

elif eleccion == "🚀 Generador de Ideas para Startups":
    sector = st.text_input("🌎 Sector de la startup")
    if st.button("Generar Ideas"):
        prompt = f"Propón ideas innovadoras para startups en el sector {sector}."
        st.write(generar_respuesta(prompt))
