"""
while condicion:
    #codigo a ejecutar
    
"""

"""
import getpass
#Bienvenida
password = getpass.getpass ("Ingrese su clave a continuación: \n")

while len (password) < 6:
    password = getpass.getpass ("Ingrese su clave con largo igual o superior a seis caracteres: \n")

while password != "Hola Mundo":
    password = getpass.getpass ("No adivinaste la constraeña. Ingrese su clave nuevamente: \n")
    
print("¡Contraseña correcta! Te doy la bienvenida")
#Resto del programa
"""
#ITERACIÓN
"""
i = 0
intentos = 10-i
while i < 10: 
    intentos = 10-i
    print(f"Te quedan {intentos} intentos")
    i = i+1 # o i+=1 (incrementar) si no se incrementa el valor de i el loop será infinito

print("Fin del programa")
"""

"""
while True
print ("acciones infinitas")
if condición:
    break
    else: 
        break (cierre del bucle)   
"""

"""
OPERADORES DE ASIGNACIÓN
= asignación
+= incremento y asignación
-= decremento y asignación
*= multiplicación y asignación
/= división y asignación
"""

saludo = "hola"
saludo = saludo +" mundo" 
print(saludo)
saludo += " chao"
print(saludo)