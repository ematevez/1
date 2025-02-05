import google.generativeai as genai

# Configurar la API key
genai.configure(api_key="AIzaSyCXBTKaMLsAm9RUnYgfqbQx9G9r-MxiWCk")

# Crear el modelo
model = genai.GenerativeModel("gemini-1.5-flash")

# Pedir input al usuario
prompt = input("Ingresa tu prompt: ")

# Generar respuesta
response = model.generate_content(prompt)

# Imprimir respuesta
print("\nRespuesta del modelo:\n")
print(response.text)
