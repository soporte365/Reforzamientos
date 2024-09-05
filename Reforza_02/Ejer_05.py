"""
5. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
"""

class Alumno:

    def __init__(self, nombre, edad, nota_f):
        self.nombre = nombre
        self.edad = edad
        self.nota_f = nota_f

    def impAtri(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota_f}")

    def resul(self):
        if self.nota_f >=11:
            print(f"El alumno {self.nombre}, ha aprobado con una nota de:{self.nota_f}, puntos")
        else:
            print(f"El alumno {self.nombre}, ha reprobado con una nota de:{self.nota_f}, puntos")




Alumno1 = Alumno("Carlos", 37, 15)
Alumno1.impAtri()
Alumno1.resul()

Alumno2 = Alumno("Maria",24,11)
Alumno2.impAtri()
Alumno2.resul()

Alumno3 = Alumno("Pedro",32,10)
Alumno3.impAtri()
Alumno3.resul()
