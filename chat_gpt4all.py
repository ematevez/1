import openai

# Configurar OpenRouter como base de la API
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"  # Reemplaza con tu API Key

# Definir los mensajes de la conversación
messages = [
    {"role": "system", "content": "Eres un asistente útil."},
    {"role": "user", "content": "Hola, ¿cómo estás?"}
]

# Realizar la solicitud al modelo
response = openai.ChatCompletion.create(
    model="openai/gpt-3.5-turbo",  # Modelo que deseas usar
    messages=messages
)

# Obtener la respuesta del asistente
reply = response["choices"][0]["message"]["content"]

# Imprimir la respuesta
print(reply)

            # Mostrar la respuesta del asistente
            st.markdown(reply)

    # Agregar la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": reply})
