import json

def cargar_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def personas_por_deporte(data, deporte):
    for persona in data.values():
        if deporte in persona["deportes"]:
            print(f'{persona["nombres"]} {persona["apellidos"]}')

def personas_por_rango_edad(data, edad_min, edad_max):
    for persona in data.values():
        if edad_min <= persona["edad"] <= edad_max:
            print(f'{persona["nombres"]} {persona["apellidos"]}')

# Ejemplo de uso
data = cargar_json("personas.json")
deporte = input("Ingrese un deporte: ")
personas_por_deporte(data, deporte)

edad_min = int(input("Edad mínima: "))
edad_max = int(input("Edad máxima: "))
personas_por_rango_edad(data, edad_min, edad_max)
