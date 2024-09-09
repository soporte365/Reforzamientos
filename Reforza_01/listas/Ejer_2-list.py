"""
2. Agregar 4 Objetos nuevos a tu lista (append) y quitar 2 elementos de tu nueva lista ítems
por valor, no por índice. Mostrar la lista final por consola
"""
class nuevos:

    def __init__(self, vary):
        self.vary = vary
# Esta funcion nos permite comprar los elementos de los objetos dentro de la lista
    def __eq__(self, other):
        return self.vary == other.vary

#inicializamos la lista
lista = []

# Creamos un loop para ingresar hasta 4 valores.
# def agreEle():
#     for cosas in range (0,4):
#         coss = nuevos(input("Ingrese una palabra: "))
#         lista.append(coss)
#
# def impriLis():
#     i = 0
#     while i < len(lista):
#         print("palabras:", lista[i].vary)
#         i += 1
#
# def remLis():
#     elim = nuevos(input('Ingrese la palabra a eliminar: '))
#     lista.remove(elim)
#     print(f"Palabra eliminada: {elim.vary}")
#     print("Lista con palabras restantes: ")
#     impriLis()

# SIN USO DE FUNCIONES
for cosas in range(0, 4):
    coss = nuevos(input("Ingrese una palabra: "))
    lista.append(coss)

i = 0
while i < len(lista):
    print("palabras:", lista[i].vary)
    i += 1

elim = nuevos(input('Ingrese la palabra a eliminar: '))
lista.remove(elim)
print(f"Palabra eliminada: {elim.vary}")
print("Lista con palabras restantes: ")
#impriLis()
i = 0
while i < len(lista):
    print("palabras:", lista[i].vary)
    i += 1

# # Ingresar datos
# agreEle()
# # Imprimimos la lista original
# impriLis()
#
# # Imprimimos la lista original
# remLis()