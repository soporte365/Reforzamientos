"""
6. Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal.
"""
from Reforza_01.Ejer_04 import lista

lista1 = ["Matematica","Fisica","Geografia","Castellano","Matematica"]

# imprime la cantidad de veces que se repite un curso
print(f"el curso de matematica se repite {lista1.count("Matematica")} veces")

print("Lista antes de borrar")
print(lista1)

# Eliminar elemento por indice
lista1.pop(0)
print("Lista luego de borrar")
print("Lista numero 1:", lista1)

lista2 = []
lista2.append(2.5)
lista2.append(3.2)
lista2.append(9.1)
lista2.append(5)
lista2.append(4)
lista2.append(3)
lista2.append("Madera")
lista2.append("Pierda")
lista2.append("Oro")
print("Lista numero 2: ", lista2)

print(lista1 + lista2)