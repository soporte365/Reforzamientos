"""
1. Crear una lista de 6 objetos y mostrar en pantalla (ítems de cursos que lleves o hayas
llevado en la universidad) e Invierte y muestra en consola tu lista de cursos.

"""
from operator import length_hint


#Creamos el objeto cursos
class cursos:

    def __init__(self, nom_cur):
        self.nom_curso = nom_cur

#inicializamos la lista
lista = []

# Creamos un loop para ingresar hasta 6 materias.
for curss in range (0,6):
    #nom = input("Ingrese el nombre del curso: ")
    cur = cursos(input("Ingrese el nombre del curso: "))
    lista.append(cur)

# Creamos una funcion para imprimir lo que esta dentro de la lista
def imp_lis():
    i=0
    while i <len(lista):
        print("Curso registrado:", lista[i].nom_curso)
        i+=1
#Imprimimos la lista
print("Lista Original:")

imp_lis()

for k in range(len(lista) //2):
    lista[k], lista[len(lista) -k -1] = lista[len(lista) -k -1], lista[k]

print("Lista Invenrtida:")
imp_lis()


