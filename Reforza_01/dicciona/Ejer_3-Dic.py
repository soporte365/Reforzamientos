"""
3. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor de
salario en consola.
var[‘key’] = tuValor
"""
# Dicionario inicial
dicio = {"Nombre":"Juan","Apellido":"Perez", "Salario":1500,"Edad":34}

# imprime el diccionario inicial
print(dicio)

#Se anexa nuevos valores
dicio["dni"]=123456789
print("Se ha añadido un nuevo valor")
print(dicio)

# Mostrar solo el salario
print("el salario es:", dicio.get("Salario"))

