""""
9. Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())

"""
lista = [5.3, "madre", 3.5, True, [2, "lol", 2.5], 3]

# Prueba uno
i = 0
while i < len(lista):
    print(type(lista[i]))
    i += 1

# Prueba dos
for e in lista:
    print(type(e))
