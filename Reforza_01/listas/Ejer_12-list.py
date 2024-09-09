"""
12. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar una cadena (string) en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del
"""
lista = []

# Llena la lista con numeros imapres
for i in range(0,31):
    if i % 2 == 1: # Siempre y cuando el valor del resultado de la comparación sea 1 llena la tabla
        lista.append(i)

# Imprime lista con numeros impares
print("Lista llena")
print(lista)

# imgrensamos nuevos valores
lista.append(3.5)
lista.append(3.5)
lista.append(3.5)
print("Lista actualziada con los floats")
print(lista)

# Insertar el string en la posición 3
lista.insert(3,"Hola")
print("Lista actualziada con palabra Hola")
print(lista)

# Eliminar el string en la posición 3
del lista[3]
print("Lista actualziada sin palabra Hola")
print(lista)

