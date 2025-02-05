# from transformers import pipeline

# # Cargar un modelo gratuito (por ejemplo, GPT-2)
# generator = pipeline("text-generation", model="gpt2")

# # Realizar una consulta
# response = generator("¿Qué opinas sobre el clima hoy?", max_length=50, num_return_sequences=1)
# print(response[0]['generated_text'])

from transformers import AutoModelForCausalLM, AutoTokenizer

# Modelo a utilizar (puedes cambiarlo a otro modelo público)
model_name = "gpt2"

# Cargar el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Texto inicial para generar contenido
input_text = "por que sale el sol?"

# Tokenizar la entrada
inputs = tokenizer(input_text, return_tensors="pt")

# Generar texto
outputs = model.generate(
    inputs.input_ids,
    max_length=50,           # Longitud máxima del texto generado
    num_return_sequences=1,  # Número de respuestas generadas
    temperature=0.7,         # Controla la creatividad (valores más bajos = más conservador)
    top_p=0.9,               # Núcleo de muestreo (probabilidad acumulada)
    do_sample=True           # Generar muestras (en lugar de texto determinista)
)

# Decodificar y mostrar el texto generado
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Texto generado:")
print(generated_text)
