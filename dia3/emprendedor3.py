precio = input("Ingresa el precio de suscripción \n")
precio = int(precio)
usuarios = input("Ingresa el número de usuarios \n")
usuarios = int(usuarios)
gasto = input ("Ingresa el gasto total \n")
gasto = int(gasto)

utilidades = (precio * usuarios) - gasto

preuti = input("Ingresa las utilidades del año pasado \n")
preuti = float(preuti)

diferencia = utilidades - preuti
diferencia = round(diferencia,2)
print(f"Las utilidades son {utilidades} pesos")
print(f"Y la diferencia entre las utilidades del año pasado y las actuales es de {diferencia} pesos")