from transformers import pipeline

# Especificar que usas PyTorch para cargar el modelo
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", framework="pt")

# Realizar una consulta
response = chatbot("¿por que el cielo es azul?", max_length=50)

print(response[0]["generated_text"])

