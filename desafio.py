from gpt4all import GPT4All

# Cargar el modelo de GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")  # Asegúrate de tener suficiente espacio para el modelo

# Función para generar tareas
def generar_tareas(prompt):
    """
    Genera tareas pendientes basadas en un prompt dado.
    """
    with model.chat_session():  # Crear una sesión de chat con el modelo
        respuesta = model.generate(
            prompt,
            max_tokens=512,  # Ajusta el límite de tokens según sea necesario
        )
    return respuesta

# Solicitar entrada del usuario
descripcion_evento = input("Describe el evento o reunión: ")

# Crear un prompt específico para generar tareas pendientes
prompt_tareas = f"""
A partir de la siguiente descripción de un evento, genera una lista de tareas pendientes:
Descripción del evento: {descripcion_evento}
Tareas:
"""

# Generar las tareas
tareas_generadas = generar_tareas(prompt_tareas)

# Mostrar las tareas generadas
print("\nTareas pendientes generadas automáticamente:")
print(tareas_generadas)
