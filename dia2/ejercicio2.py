#división de integers siempre da un float
print (100/20)
#se pueden hacer operaciones entre integers y float
print (10+3.5)
print (10-3.5)
print (10*3.5)
print (10/3.5)

#string usa comilla simple o doble, pero tiene que empezar y terminar igual ->es una cadena de caracteres
nombre = "lars" # es igual que nombre = 'lars'
edad = "32"
numero = 100
print(edad) #imprime el contenido de una variable
#DUPLICACIÓN -> repite el contenido de una variable string 
print(type (edad)) #<class 'str'>
print(3*edad)
print(type (numero)) #<class 'int'>
print(3*numero)

#count ->contar cuantas veces aparece un caracter alfanumérico en un string
print("Abracadabra".count("a")) #A=!a
#length no es un método, pero sirve para contar elementos en un objeto
print(len("17.960.494-9"))
#print(len(179604949)) #un número no es un objeto

#método upper y lower
print("AbrAcAdAbrA".upper()) #mayúscula
print("AbrAcAdAbrA".lower()) #minúscula

#método title
print("AbrAcAdAbrA".title()) #mayúscula y el resto minúscula

#join -> unir elementos separados // print("elemento separador".join(["x", "y", "z"]))
print(", ".join(["a","b","c"]))

#\n -> salto de línea
print("esto es \nun salto de línea")

#valores lógicos Booleanos (true/false)

#tipos de datos
entero = 13
decimal = 13.31
cadena = "esto es una cadena"
booleanos = True #o False

print(type(entero)) #<class 'int'>
print(type(decimal)) #<class 'float'>
print(type(cadena)) #<class 'str'>
print(type(booleanos)) #<class 'bool'>

#precision de datos
promedio = (4+5+7)/3
print(f"el promedio es {promedio}")
print(f"resulta de la division {promedio:.4f}")
print(f"resulta de la division {round(promedio,3)}") #round además de limitar la cantidad de decimales, también aproxima

#INGRESO DE DATOS (INPUT)
nombre = input("Ingrese su nombre ")
print(f"Hola {nombre}")
nombre = input("Ingrese su edad ")
print(f"Tienes {edad} años")