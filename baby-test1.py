
import babyagi
import google.generativeai as genai

# Configurar la API key de Google Gemini
API_KEY = "AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk"

@babyagi.register_function()
def generar_contenido(prompt):
    API_KEY = "AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk"
    # Importar y configurar genai dentro de la función
    import google.generativeai as genai
    genai.configure(api_key=API_KEY)

    # Crear el modelo
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generar respuesta
    response = model.generate_content(prompt)
    return response.text

# Ejecutar BabyAGI con dashboard
if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
