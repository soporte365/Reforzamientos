"""
1. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico.

"""

class nume:

    def __init__(self, var1 = 2):
        self.var1 = var1

    def convierte(self):
        return self.var1 ** 3

    def convierte2(self):
        return self.convierte() ** 2

    def solicitu(self):
        varA = int(input("Ingrese un valor positivo mayor que cero: "))
        if varA <= 0:
            print("Error no puedes ingresar un valor negativo o menor que cero")
        else:
            self.var1 = varA


numer = nume()
print("El numero entero incial es: ", numer.var1)
print("El numeor elevado al cubo es: " ,numer.convierte())
print("El resultado elevado al Cuadrado es: " ,numer.convierte2())
numer.solicitu()
print("El numero entero incial es: ", numer.var1)
print("El numeor elevado al cubo es: " ,numer.convierte())
print("El resultado elevado al Cuadrado es: " ,numer.convierte2())
