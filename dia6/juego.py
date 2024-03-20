from random import choice
nombre = input("Ingrese su nombre a continuación: \n")
print(f"Hola {nombre}, este es el juego del Cachipún, donde tendrás que elegir entre tres jugadas y vencer al computador.")
cachipun = ["Piedra","Papel","Tijera"]
computador=choice(cachipun)

usuario=input("Ingresa tu jugada (Piedra, Papel o Tijera): \n")
usuario = usuario.title()

while usuario != "Piedra" and usuario != "Papel" and usuario != "Tijera":
    print("Jugada no válida")
    usuario=input("Ingresa tu jugada (Piedra, Papel o Tijera): \n")

print(f"Jugaste: {usuario}")
print(f"El computador jugó: {computador}")

if usuario == "Piedra" and computador == "Tijera":
    print("¡GANASTE!")
elif usuario == "Papel" and computador == "Piedra":
    print("¡GANASTE!")
elif usuario == "Tijera" and computador == "Papel":
    print("¡GANASTE!")
elif usuario == computador:
    print("¡EMPATE!")
else:
    print("¡PERDISTE!")