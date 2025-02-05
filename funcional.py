# from gpt4all import GPT4All

# model = GPT4All("gpt4all-lora-quantized.bin")  # Ruta al archivo del modelo
# response = model.generate("¿Cómo estás?")
# print(response)


from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
promt = input("Ingresa consulta: ")
with model.chat_session():
    print(model.generate(promt, max_tokens=1024))