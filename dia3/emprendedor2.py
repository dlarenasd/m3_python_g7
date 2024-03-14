precio = input("Ingresa el precio de suscripción en CLP \n")
precio = float(precio)
usuarios = input("Ingresa el número de usuarios normales \n")
usuarios = int(usuarios)
usuariosPremium = input("Ingresa el número de usuarios Premium \n")
usuariosPremium = int(usuariosPremium)
gastoTotal = input ("Ingresa el gasto total en CLP\n")
gastoTotal = float(gastoTotal)

utilidades = (precio * usuarios)+((precio*1.5)*usuariosPremium) - gastoTotal
print(f"Las utilidades son {utilidades} CLP")