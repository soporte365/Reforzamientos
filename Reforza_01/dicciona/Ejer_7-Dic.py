"""
7. Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento (uno) usando la palabra reservada del.
- Comprobar que no existe este departamento borrado dentro del diccionario.
"""
# Dicionario inicial
dicio = {"Departamento1":"Amazonas","Departamento2":"Áncash", "Departamento3":"Apurímac","Departamento4":"Ica",
         "Departamento5": "Lambayeque", "Departamento6":"Lima"}

# imprime el diccionario inicial
print(dicio)

#Se elimina el valor edad
#dicio.pop("Edad")
del dicio["Departamento3"]
print("Se ha eliminado un  valor")
print(dicio)