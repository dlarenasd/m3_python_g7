import math
radio = input("Ingresa el radio del planeta en Kilometros \n")
radio = float(radio)
constante = input("Ingresa la constante g (recuerda usar punto y no coma) \n")
constante = float(constante)
velocidad = (math.sqrt(2*(radio*1000)*constante))
velocidad = round(velocidad,1)

print(f"La velocidad de escape es {velocidad} [m/s]")
