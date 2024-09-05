""""
3. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""

class informacion:

    def __init__(self, nombre="", apellido="", edad=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def ingreNom(self):
        self.nombre = input("Ingrese su Nombre: ")
        self.apellido = input("Ingrese su Apellido: ")

    def ingreEda(self):
        self.edad = int(input("Ingrese su Edad: "))
        #if edad <= 0:
         #   print("Error ingrese un valor positivo mayor a cero")
        #else:
        #    self.edad = edad

    def impri(self):
        diccio = {"Nombre": self.nombre,
                  "Apellido": self.apellido,
                  "Edad": self.edad}
        print(diccio)


persona = informacion()
persona.ingreNom()
persona.ingreEda()

persona1 = informacion()
persona1.ingreNom()
persona1.ingreEda()

persona.impri()
persona1.impri()

