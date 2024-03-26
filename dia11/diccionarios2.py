from os import system
personajes ={}

cantidad_de_personajes = int(input("Ingrese cantidad de personajes a ingresar: "))

for i in range(cantidad_de_personajes):
    

    personaje = {"Nombre":"",
                "Etnia": "",
                "Ojos":"",
                "Orden":""}

    """ 
    for clave in personaje:
        personaje[clave]= input(f"Ingrese {clave} del personaje: \n")
        
    print(personaje)
    """

    for key in personaje.keys():
        
        personaje[key]= input(f"Ingrese {key} del personaje: \n") #incluir los valores a través de las claves
    print(personaje)

    for valor in personaje.values(): #acceder a los valores de nuestro diccionario
        print(valor)
        
    print("")

    for clave, valor in personaje.items():
        print(f"clave {clave} - valor {valor}")


        
    personajes[personaje["Nombre"]]=personaje  
print(personajes) #{'Shallan': {'Nombre': 'Shallan', 'Etnia': 'Veden', 'Ojos': 'Claros', 'Orden': 'Tejedora de luz'}}

"""
{'Kaladin': {'Nombre': 'Kaladin', 'Etnia': 'Alezi', 'Ojos': 'Oscuros', 'Orden': 'Corredores del Viento'}, 
'Shallan': {'Nombre': 'Shallan', 'Etnia': 'Veden', 'Ojos': 'Claros', 'Orden': 'Tejedora de luz'}, 
'Lift': {'Nombre': 'Lift', 'Etnia': 'Reshi', 'Ojos': 'Oscuros', 'Orden': 'Danzante del filo'}}
"""
#Acceder a un diccionario
personajes["Kaladin"]#-->{'Nombre': 'Kaladin', 'Etnia': 'Alezi', 'Ojos': 'Oscuros', 'Orden': 'Corredores del Viento'}
personajes["Kaladin"] ["Nombre"] #--> "Kaladin"

system("cls")