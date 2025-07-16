import requests

def conectar_api(url):
    respuesta = requests.get(url)
    datos = respuesta.json()
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Ejemplo: API de chiste aleatorio
conectar_api("https://api.chucknorris.io/jokes/random")

# Ejemplo: API de edad por nombre
conectar_api("https://api.agify.io/?name=juan")

# Ejemplo: API de nacionalidad por nombre
conectar_api("https://api.nationalize.io/?name=michael")
