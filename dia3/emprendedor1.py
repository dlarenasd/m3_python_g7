precio = input("Ingresa el precio de suscripción \n")
precio = int(precio)
usuarios = input("Ingresa el número de usuarios \n")
usuarios = int(usuarios)
gasto = input ("Ingresa el gasto total \n")
gasto = int(gasto)

utilidades = (precio * usuarios) - gasto
print(f"Las utilidades son {utilidades} pesos")