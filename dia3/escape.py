import math
radioPlaneta = input("Ingresa el radio del planeta en Kilometros \n")
radioPlaneta = float(radioPlaneta)
constanteGravitacional = input("Ingresa la constante g (recuerda usar punto y no coma) \n")
constanteGravitacional = float(constanteGravitacional)
velocidadEscape = (math.sqrt(2*(radioPlaneta*1000)*constanteGravitacional))

print(f"La velocidad de escape es {round(velocidadEscape,1)} [m/s]")
