import json
from gpt4all import GPT4All

# Cargar el modelo de GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

# Función para generar tareas en formato JSON
def generar_tareas_json(prompt):
    """
    Genera una tarea pendiente en formato JSON utilizando el modelo GPT4All.
    """
    with model.chat_session():
        respuesta = model.generate(prompt, max_tokens=512, )
    return respuesta

# Función para limpiar y procesar la respuesta JSON
def procesar_tarea_json(respuesta_json):
    """
    Procesa una respuesta en formato JSON y extrae información clave.
    Intenta limpiar el contenido si no es un JSON válido.
    """
    try:
        # Buscar el contenido que parece un JSON
        inicio = respuesta_json.find("{")
        fin = respuesta_json.rfind("}") + 1
        json_limpio = respuesta_json[inicio:fin]

        # Convertir el contenido a un diccionario
        tarea = json.loads(json_limpio)  # Convertir de JSON a diccionario
        titulo = tarea.get("titulo", "Título no especificado")
        descripcion = tarea.get("descripcion", "Descripción no especificada")
        fecha = tarea.get("fecha", "Fecha no especificada")
        prioridad = tarea.get("prioridad", "Prioridad no especificada")
        
        # Imprimir los datos extraídos
        print("\nInformación clave extraída:")
        print(f"Título: {titulo}")
        print(f"Descripción: {descripcion}")
        print(f"Fecha: {fecha}")
        print(f"Prioridad: {prioridad}")
    except json.JSONDecodeError as e:
        print("Error: La respuesta no es un JSON válido.")
        print(f"Detalles del error: {e}")
        print("\nRespuesta completa generada:")
        print(respuesta_json)

# Solicitar al usuario la descripción de la tarea
descripcion_usuario = input("Ingresa la descripción de la tarea: ")

# Crear el prompt dinámico a partir de la descripción ingresada
prompt_json = f"""
Genera una tarea pendiente para una reunión de equipo en formato JSON.
El formato esperado es el siguiente:
{{
    "titulo": "string",
    "descripcion": "string",
    "fecha": "DD-MM-AAAA",
    "prioridad": "1-Alta/2-Media/3-Baja"
}}
Ejemplo:
{{
    "titulo": "Revisión de métricas anuales",
    "descripcion": "Analizar las métricas del año para planificar objetivos del próximo año.",
    "fecha": "2024-12-15",
    "prioridad": "Alta"
}}
Ahora genera la tarea basada en la siguiente descripción:
"{descripcion_usuario}"
"""

# Generar la tarea en formato JSON
respuesta_generada = generar_tareas_json(prompt_json)
print("\nRespuesta generada (JSON):")
print(respuesta_generada)

# Procesar la respuesta JSON
procesar_tarea_json(respuesta_generada)
