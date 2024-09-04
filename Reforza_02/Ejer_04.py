"""
4. Crear una clase llamada círculo que contenga radio en su constructory que
contenga un método área que devuelva el área de un círculo. Aplicar
excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.Instanciar
la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""

class circulo:

    def __init__(self, radio=0):
        self.radio = radio

    def solradio(self):
            try:
                self.radio = int(input("Ingrese su el radio: "))
            except ValueError:
                print("ingrese solo numeros")
            else:
              return  self.radio

   # def revis(self):
   #    if self.radio <= 0:
   #        print("Erro el valor debe ser mayor que 0")
   #    elif self.radio == str(self.radio):
   #         print("Erro debe ingresar un valor numerico")
   #     else:
   #         return self.radio

    def calArea(self):
        return round(3.14 * (self.radio ** 2))

    def CalDiam(self):
        return  round(2 * 3.14 * self.radio)


circulo1 = circulo()
circulo1.solradio()
print("El área del círuclo es: ", circulo1.calArea())
print("El Périmetroi del círuclo es: ", circulo1.CalDiam())

