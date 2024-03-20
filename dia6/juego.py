from random import choice
#BIENVENIDA
nombre = input("Ingrese su nombre a continuación: \n")
print(f"Hola {nombre}, este es el juego del Cachipún, donde tendrás que elegir entre tres jugadas y vencer al computador.")

#DEFINICIÓN DE VARIABLES BASE
cachipun = ["Piedra","Papel","Tijera"]
computador=choice(cachipun)

#INGRESO DE JUGADA
usuario=input("Ingresa tu jugada (Piedra, Papel o Tijera): \n")
usuario = usuario.title()

#VALIDACIÓN
while usuario != "Piedra" and usuario != "Papel" and usuario != "Tijera":
    print("Jugada no válida")
    usuario=input("Ingresa tu jugada (Piedra, Papel o Tijera): \n")
    usuario = usuario.title()
    
#OUTPUT
print(f"Jugaste: {usuario}")
print(f"El computador jugó: {computador}")

#CONDICIONES
if usuario == computador:
    print("¡EMPATE!")
elif (usuario == "Piedra" and computador == "Tijera") or\
(usuario == "Papel" and computador == "Piedra") or \
(usuario == "Tijera" and computador == "Papel"):
    print("¡GANASTE!")  
else:
    print("¡PERDISTE!")