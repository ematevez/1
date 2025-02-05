import google.generativeai as genai
import babyagi

# Configurar la API key
genai.configure(api_key="AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk")

# Registrar la función en BabyAGI
@babyagi.register_function()
def generar_contenido(prompt):
    # Crear el modelo
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Generar respuesta
    response = model.generate_content(prompt)
    return response.text

# Ejemplo de uso
if __name__ == "__main__":
    prompt = input("Ingresa tu prompt: ")
    resultado = generar_contenido(prompt)
    print("\nRespuesta del modelo:\n")
    print(resultado)
