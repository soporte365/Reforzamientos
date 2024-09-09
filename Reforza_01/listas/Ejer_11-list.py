"""
11. Mostrar sólo los datos comprendidos entre la posición 10 y 35
"""

lista = []

# Llena la lista con numeros
for datos in range (0,35):
    datos += 1
    lista.append(datos)

# Imprime la lista
print("Lista llena")
print(lista)

# Imprime lo solicitado
print("Lista entre el rango 10 y 35")
print(lista[9:35])
