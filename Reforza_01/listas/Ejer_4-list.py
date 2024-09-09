"""
4. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista luego elimina el primer ítem de la lista usando debidamente su índice.

"""
lista = ["Matematica","Fisica","Geografia","Castellano","Matematica"]

# imprime la cantidad de veces que se repite un curso
print(f"el curso de matematica se repite {lista.count("Matematica")} veces")

print("Lista antes de borrar")
print(lista)

# Eliminar elemento por indice
lista.pop(0)
print("Lista luego de borrar")
print(lista)