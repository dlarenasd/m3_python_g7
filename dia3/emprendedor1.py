precio = input("Ingresa el precio de suscripción en CLP\n")
precio = float(precio)
usuarios = input("Ingresa el número de usuarios \n")
usuarios = int(usuarios)
gasto = input ("Ingresa el gasto total en CLP \n")
gasto = float(gasto)

utilidades = (precio * usuarios) - gasto
print(f"Las utilidades son {utilidades} CLP")