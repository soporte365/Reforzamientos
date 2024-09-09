""""
13. Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media
de los números.
"""

lista = []
# Creamos un loop para ingresar hasta 10 materias.
for curss in range (10):
    valor = int(input("Ingrese el valor: "))
    lista.append(valor)


print("Lista llena")
print(lista)
print("suma de los valores de la lista: ", sum(lista))
print("La media de los valores de la lista es: ", (sum(lista) / len(lista)))