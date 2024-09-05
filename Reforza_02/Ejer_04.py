"""
4. Crear una clase llamada círculo que contenga radio en su constructor y que
contenga un método área que devuelva el área de un círculo. Aplicar
excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.Instanciar
la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""

class circulo:

    def __init__(self, radio):
        self.radio = radio

   # def solradio(self):
   #        try:
   #             self.radio = int(input("Ingrese el radio: "))
   #         except ValueError:
   #             print("ingrese solo numeros")
   #         else:
   #           return  self.radio

    def calArea(self):
       # if self.solradio() == self.radio:
            return round(3.14 * (self.radio ** 2))

    def CalDiam(self):
       # if self.solradio()== self.radio:
            return  round(2 * 3.14 * self.radio)

try:
 circulo1 = circulo(int(input("Ingrese un numero:")))
except ValueError:
    print("ingrese solo numeros")
else:
    print("El área del círuclo 1 es: ", circulo1.calArea())
    print("El Périmetroi del círuclo 1 es: ", circulo1.CalDiam())


#circulo2 = circulo()
#circulo2.solradio()
#print("El área del círuclo 2 es: ", circulo1.calArea())
#print("El Périmetroi del círuclo 2 es: ", circulo1.CalDiam())
