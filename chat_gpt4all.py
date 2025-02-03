import os
import urllib.request

# Definir ruta y enlace del modelo
MODEL_PATH = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
MODEL_URL = "https://gpt4all.io/models/Meta-Llama-3-8B-Instruct.Q4_0.gguf"

# Descargar si no existe
if not os.path.exists(MODEL_PATH):
    with st.spinner("Descargando modelo... Esto puede tardar unos minutos."):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
