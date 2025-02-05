import json
import re
from gpt4all import GPT4All
from datetime import datetime

# Cargar el modelo de GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
# model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf.cpu")


# Función para generar tareas en formato JSON
def generar_tareas_json(descripcion):
    """
    Genera una tarea pendiente en formato JSON utilizando una descripción personalizada y GPT4All.
    """
    prompt = f"""
    Genera una tarea pendiente para una reunión de equipo en formato JSON.
    El formato esperado es el siguiente:
    {{
        "titulo": "string",
        "descripcion": "string",
        "fecha": "YYYY-MM-DD",
        "prioridad": "Alta/Media/Baja"
    }}
    Ahora genera la tarea basada en la siguiente descripción:
    "{descripcion}"
    """

    with model.chat_session():
        respuesta = model.generate(
            prompt,
            max_tokens=512,
        )
    return respuesta


# Función para procesar la respuesta JSON y guardar en archivos
def procesar_tarea_json(respuesta_json):
    """
    Procesa una respuesta en formato JSON, extrae información clave y guarda en .json y .txt.
    """
    try:
        # Extraer el bloque JSON de la respuesta
        match = re.search(r"\{.*\}", respuesta_json, re.DOTALL)
        if not match:
            raise ValueError("No se encontró un bloque JSON en la respuesta.")

        tarea = json.loads(match.group())  # Convertir de JSON a diccionario

        # Extraer datos
        titulo = tarea.get("titulo", "Título no especificado")
        descripcion = tarea.get("descripcion", "Descripción no especificada")
        fecha = tarea.get("fecha", "Fecha no especificada")
        prioridad = tarea.get("prioridad", "Prioridad no especificada")

        # Crear nombres de archivo únicos
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo_json = f"tarea_{timestamp}.json"
        archivo_txt = f"tarea_{timestamp}.txt"

        # Guardar en archivo .json
        with open(archivo_json, "w", encoding="utf-8") as file_json:
            json.dump(tarea, file_json, indent=4, ensure_ascii=False)

        # Guardar en archivo .txt
        with open(archivo_txt, "w", encoding="utf-8") as file_txt:
            file_txt.write(f"Título: {titulo}\n")
            file_txt.write(f"Descripción: {descripcion}\n")
            file_txt.write(f"Fecha: {fecha}\n")
            file_txt.write(f"Prioridad: {prioridad}\n")

        print("\nLos resultados se han guardado correctamente:")
        print(f"- Archivo JSON: {archivo_json}")
        print(f"- Archivo TXT: {archivo_txt}")
    except json.JSONDecodeError as e:
        print(f"Error: La respuesta no es un JSON válido. Detalles: {e}")
    except Exception as e:
        print(f"Error: {e}")


# Solicitar descripción de la tarea al usuario
descripcion_tarea = input("Ingresa la descripción de la tarea: ")

# Generar la tarea en formato JSON
respuesta_generada = generar_tareas_json(descripcion_tarea)
print("\nRespuesta generada:")
print(respuesta_generada)

# Procesar la respuesta JSON y guardar en archivos
procesar_tarea_json(respuesta_generada)
