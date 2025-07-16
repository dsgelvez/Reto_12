def mezclar_diccionarios(dic1, dic2):
    mezcla = dic2.copy()
    mezcla.update(dic1)
    return mezcla

# Ejemplo
d1 = {'a': 1, 'b': 2}
d2 = {'b': 9, 'c': 3}
print(mezclar_diccionarios(d1, d2))  # {'b': 2, 'c': 3, 'a': 1}
