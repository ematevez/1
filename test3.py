from gpt4all import GPT4All

# Cargar el modelo
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # Carga el modelo

# Iniciar una sesión de chat
try:
    with model.chat_session() as session:
        print("ChatGPT listo para responder tus preguntas. Escribe 'salir' para terminar.\n")
        while True:
            # Solicitar una pregunta al usuario
            pregunta = input("Tú: ")

            # Verificar si el usuario quiere salir
            if pregunta.lower() == "salir":
                print("¡Hasta luego!")
                break

            try:
                # Generar la respuesta del modelo
                respuesta = session.generate(pregunta, max_tokens=1024)
                print(f"ChatGPT: {respuesta}\n")
            except Exception as e:
                print(f"Error al generar respuesta: {e}")
except Exception as e:
    print(f"Error general en el modelo: {e}")
