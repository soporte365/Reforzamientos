"""
4. Elimina el key edad tipo de tu diccionario, incluyendo su valor.
del var[‘key’]
"""

# Dicionario inicial
dicio = {"Nombre":"Juan","Apellido":"Perez", "Salario":1500,"Edad":34}

# imprime el diccionario inicial
print(dicio)

#Se elimian el valor edad
#dicio.pop("Edad")
del dicio["Edad"]
print("Se ha eliminado un  valor")
print(dicio)

