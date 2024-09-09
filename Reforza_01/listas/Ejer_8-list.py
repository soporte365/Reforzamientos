"""
8. Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el penúltimo y
último valor (por índice).
"""


lista = [5.3, False, 3.5, True, False, 3.5]

ulti = len(lista)-1
pnul = len(lista)-2
print(f"El penultimo valor de la lista es: {lista[pnul]},\n"
      f"El ultimo valor de la lista es: {lista[ulti]}")