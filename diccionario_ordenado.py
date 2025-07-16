def imprimir_valores_ascendentes(dic):
    valores_ordenados = sorted(dic.values())
    print("Valores en orden ascendente:")
    for valor in valores_ordenados:
        print(valor)

# Ejemplo
diccionario = {'a': 30, 'b': 10, 'c': 50, 'd': 20}
imprimir_valores_ascendentes(diccionario)
