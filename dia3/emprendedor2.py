precio = input("Ingresa el precio de suscripción \n")
precio = int(precio)
usuarios = input("Ingresa el número de usuarios normales \n")
usuarios = int(usuarios)
usuariosP = input("Ingresa el número de usuarios Premium \n")
usuariosP = int(usuariosP)
gasto = input ("Ingresa el gasto total \n")
gasto = int(gasto)

utilidades = (precio * usuarios)+((precio*1.5)*usuariosP) - gasto
print(f"Las utilidades son {utilidades} pesos")