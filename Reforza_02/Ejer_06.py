"""
6. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un método para mostrar los datos e indicar si la persona
es mayor de edad o no y otro método que bonificación que retornará el
20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""

class Persona:

    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mosAtr(self):
        print("Datos de la persona", sep="")
        print("Nombre:", self.nombre)
        if self.edad <= 17:
          print("Edad:", self.edad, "Menor de edad")
        elif 18 <= self.edad <= 60:
          print("Edad: ", self.edad, "Adulto")
        else:
            print("Edad:", self.edad, "Adulto Mayor")
        print("Sueldo:", self.sueldo)

    def boni(self):
         return round(self.sueldo  * 0.20)


person1 = Persona("Carlos", 37, 1500)
person1.mosAtr()
print("Bonificación del 20% del sueldo:", person1.boni())

person2 = Persona("Pedro", 17, 1025)
person2.mosAtr()
print("Bonificación del 20% del sueldo:", person2.boni())

person3 = Persona("Maria", 65, 1690)
person3.mosAtr()
print("Bonificación del 20% del sueldo:", person3.boni())