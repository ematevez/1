from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Tokenizar la entrada
input_text = "¿Qué es la vida?"
inputs = tokenizer(input_text, return_tensors="pt")

# Generar texto
outputs = model.generate(inputs['input_ids'], max_length=50)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
