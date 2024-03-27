efemerides = {}
efemerides = {"1 de enero": "Año Nuevo",
         	"27 de febrero": "Terremoto en Chile",
         	"8 de marzo": "Día de la Mujer",
         	"21 de mayo": "Glorias Navales",
         	"18 de septiembre": "Fiestas Patrias",
         	"19 de septiembre": "Glorias del Ejercito",
            "29 de octubre": "Mi cumpleaños",
         	"25 de diciembre": "Navidad",}

fecha = input("Ingrese la fecha a consultar: ").lower() #esto solicita la clave para que el programa entregue el valor


while fecha not in efemerides:
    print("Esa fecha no se encuentra en el diccionario")
    fecha = input("Ingrese la fecha a consultar: ").lower()
    
print(f"Efemérides: {efemerides[fecha]}")