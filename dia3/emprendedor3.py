precio = input("Ingresa el precio de suscripción en CLP \n")
precio = int(precio)
usuarios = input("Ingresa el número de usuarios \n")
usuarios = int(usuarios)
gasto = input ("Ingresa el gasto total en CLP\n")
gasto = int(gasto)

utilidades = (precio * usuarios) - gasto

utilidadesAnioPrevio = input("Ingresa las utilidades del año pasado en CLP\n")
utilidadesAnioPrevio = float(utilidadesAnioPrevio)

diferencia = utilidades / utilidadesAnioPrevio

print(f"Las utilidades son {utilidades} CLP")
print(f"Y la razón entre las utilidades del año pasado y las actuales es de {round(diferencia,2)}")