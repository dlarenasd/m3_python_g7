import sys


with open(sys.argv[1],"r") as file:
    texto=file.read()

cantidad_caracteres = len(set(texto))
cantidad_palabras = len(set(texto.split()))

print(f"El número de caracteres distintos es: {cantidad_caracteres}")
print(f"El número de palabras distintas del texto es: {cantidad_palabras}")