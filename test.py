import openai

# Lista de claves API
api_keys = [
"sk-Onw2d89a6X4iO3qC6mbM3PcM6tSpBz5wTkE257TRwc59283y",
"sk-yO12X2MncDEjyy5H8Cdy4Wp8xQ1HE00HUV2eQDc663x2BjYo",
"sk-tODo9EX21QENiJ62L5T09JstmdD8kPu09oXnwDO01wfdyi2w",
"sk-dZ260VUsm6FMGwie1f6gJb3ONUGlErM6TcGN62rPgo4XCaqD",
"sk-54coRUok4R7l5bqH54R3P3G1I0jyt9096a5747GHDwIo3XE8",
"sk-56sME8R80dr98IH019TM07Qz3xs7VM7GW5SCQZkW0cH2u4VT",
"sk-Gj7sO4qAlqD64tr34Id371iD8qeC2aLWUFD9j19hW66C1okI",
"sk-KtL3gZKkF9aBmXkXnvS56HPpRPUW8G9DpJ50j2k0tf3rj0HU",
"sk-p05eI5z764jvyx7B4BXTn209j63B3N09jpSEL1rCfO0u63x0",
"sk-1gbWVlRuVv2Jl97poELSVDu3j873OYF93DYibcNo3eQEibpV",
"sk-6O52kha6kTN1K454g20I3ecv1o8Kopa3hgt8q6Ly0Yj7Vm9m",
"sk-0RoKB2l5wcuy54YrExa39PY974UfTe24yl3175J01ASpeT0C",
"sk-Vi4VR476u2B6X99880q595fU50eEJph6M4vU20jm2QxZh6aR",
"sk-XD6woSBDAfwBYln0TvYmh4UEMn15824bX8Y8edUI58Z36Owd",
"sk-PX68m9eVt3LEAe864n4m6O1rn3wmYYibt6g9M97B0mxhF659",
"sk-8fSP93yD4PjdOYPKGy322y7r9vKtPU5dBtJscuk58XI40bgT"
]

# Verificar cada clave API
for key in api_keys:
    openai.api_key = key  # Configura la clave API actual
    try:
        print(f"Probando clave: {key}...")
        # Intentar listar modelos
        models = openai.Model.list()
        print(f"¡Clave funcional! Modelos disponibles con {key}:")
        for model in models['data']:
            print(model['id'])
        break  # Si funciona, salir del bucle
    except Exception as e:
        print(f"Clave {key} no es funcional. Error: {e}")

print("Prueba completada.")
