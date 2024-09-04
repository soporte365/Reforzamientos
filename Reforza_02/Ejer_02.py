"""
2. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
"""

class cadenas:

    def __init__(self, palabras):
        self.palabras = palabras

    def cambio(self):
        palb = self.palabras.split(' ')
        #print(palb)
        palb_inv = palb[::-1]
        #print(palb_inv)
        cad_inv = ' '.join(palb_inv)
        return cad_inv
        #print("Cambios :", cad_inv)



word = cadenas("Hola Pythonista, seguimos adelante")
print("Original: ", word.palabras)
print("Invertir: ", word.cambio())

word = cadenas("Hola Pythonista, seguimos adelante")
print("Original: ", word.palabras)
print("Invertir: ", word.cambio())





