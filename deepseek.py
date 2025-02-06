# Please install OpenAI SDK first: `pip3 install openai`

# from openai import OpenAI

# client = OpenAI(api_key="sk-1b5afb4284fd4b8da871c33149ff9c1c", base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# print(response.choices[0].message.content)

from openai import OpenAI

# Asegúrate de que la clave de API sea correcta
client = OpenAI(api_key="sk-1b5afb4284fd4b8da871c33149ff9c1c", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)