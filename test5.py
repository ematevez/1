from transformers import pipeline

# Cargar el pipeline de generación de texto con el modelo GPT-2 o GPT-Neo
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Realizar una consulta
response = chatbot("¿Qué es la vida?", max_length=50)

print(response[0]["generated_text"])
