nombre = input("Ingrese su nombre \n")
print(f"Hola {nombre}, a continuación le pediré algunos datos para calcular su Índice de Masa Corporal(o IMC). Recuerde que este índice es solo un número y que no representa su estado de salud, por lo que debe asesorarse con un médico u otro profesional del área.")
peso = float(input("Por favor ingrese su peso en kilogramos \n"))
altura = float(input("Por favor ingrese su altura en centímetros \n"))
while altura <=0:
    print("Valor de estatura incorrecto")
    altura = int(input("Por favor ingrese su altura en centímetros \n"))
    
altura = altura/100

indice_masa_corporal = peso/(altura**2)

print(f"Su índice de masa corporal es {round(indice_masa_corporal,2)}")

if indice_masa_corporal < 18.5:
    print("Ese valor se clasifica como Bajo Peso")
elif indice_masa_corporal >= 18.5 and indice_masa_corporal < 25:
    print("Ese valor se clasifica como Adecuado")
elif indice_masa_corporal >=25 and indice_masa_corporal < 30:
    print("Ese valor se clasifica como Sobrepeso")
elif indice_masa_corporal >=30 and indice_masa_corporal < 35:
    print("Ese valor se clasifica como Obesidad I")
elif indice_masa_corporal >=35 and indice_masa_corporal < 40:
    print("Ese valor se clasifica como Obesidad II")
else: 
    print("Ese valor se clasifica como Obesidad III")