i = 1 #0, 1 y 2
suma_notas = 0
cantidad_notas = int(input("Ingresa la cantidad de notas: \n"))
while i <= cantidad_notas:
    nota = float(input(f"Ingresa tu nota {i}: \n"))
    suma_notas = suma_notas + nota
    i+=1

print(f"El promedio de notas es: {round(suma_notas/cantidad_notas,2)} ")