"""
if ->condicional
si se cumple la condición, entonces se ejecuta el código

if condicion:
    #codigo a ejecutar si es verdadero
el tab es necesario porque es un bloque de código
elif-> añadir otra condición que puede cumplirse y ejecutar código
else ->
ejecuta el código si la condición previa no se cumple
"""
edad = int(input("Ingrese su edad: \n"))
if edad >= 18:
    print("Eres mayor de edad")
elif edad ==18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")

if edad == 0:
    print("Tu edad es 0")
elif edad % 2 ==0:
    print("Tu edad es par")
print("Fin del programa")