import json
from datetime import datetime

def convertir_fecha(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

def analizar_alertas(data):
    campos_alerta = {
        "alertAlertas": "Alerta general",
        "alertPrecip": "Lluvias",
        "alertVelViento": "Vientos fuertes",
        "alertTmpMax": "Temperatura máxima",
        "alertTmpMin": "Temperatura mínima"
    }

    for campo, descripcion in campos_alerta.items():
        print(f"\nRevisando {descripcion}:")
        for dia, valor in data[campo].items():
            if valor == "X":
                indice = str(dia)
                fecha = convertir_fecha(data["dt"][indice])

                if campo == "alertPrecip":
                    dato = f"Lluvia: {data['prcp'][indice]} mm"
                elif campo == "alertVelViento":
                    dato = f"Velocidad del viento: {data['velViento'][indice]} m/s"
                elif campo == "alertTmpMax":
                    dato = f"Temp. máxima: {data['tmpMax'][indice]} °C"
                elif campo == "alertTmpMin":
                    dato = f"Temp. mínima: {data['tmpMin'][indice]} °C"
                else:
                    dato = "Sin dato adicional"

                print(f"Fecha: {fecha} - {descripcion} -> {dato}")

with open("clima.json", "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

analizar_alertas(data)
