# RETO 12 - Programación con Diccionarios y JSON

Este reto incluye ejercicios que usan diccionarios, archivos JSON y consumo de APIs.

---

## Punto 1: Imprimir valores de un diccionario en orden ascendente

Se creó una función que recibe un diccionario y muestra sus valores ordenados de menor a mayor.

**Archivo:** `diccionario_ordenado.py`

---

## Punto 2: Mezclar dos diccionarios

Se define una función que recibe dos diccionarios y retorna uno nuevo combinando las llaves de ambos.  
Si hay claves repetidas, se mantiene el valor del primer diccionario.

**Archivo:** `mezclar_diccionarios.py`

---

## Punto 3: Leer y filtrar desde JSON

Usando el archivo `personas.json`, el programa:

- Imprime los nombres completos de las personas que practican un deporte ingresado por el usuario.
- Imprime los nombres completos de las personas dentro de un rango de edad dado.

**Archivo:** `filtrar_personas.py`  
**Datos:** `personas.json`

---

## Punto 4: Conexión con APIs

Se conectaron 3 APIs públicas y se imprimieron los pares `clave: valor` de cada respuesta:

1. [Chuck Norris Jokes API](https://api.chucknorris.io)
2. [Agify (Edad por nombre)](https://api.agify.io)
3. [Nationalize (Nacionalidad por nombre)](https://api.nationalize.io)

**Archivo:** `APIS.py`

---

## Punto 5: Análisis de alertas climáticas (JSON)

Se analiza un archivo JSON con el pronóstico del clima durante 8 días.

Se identifican alertas de:
- Lluvias
- Vientos fuertes
- Temperaturas extremas (mínimas y máximas)
- Alertas generales

Para cada alerta se imprime:
- Fecha del fenómeno
- Tipo de alerta
- Valor del parámetro relevante

**Archivos:**
- `alertas_clima.py`
- `clima.json`


