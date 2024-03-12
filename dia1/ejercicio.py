#esto es un comentario de una sola línea
"""
comentario
de más 
de una 
línea
"""
print ("texto de prueba")
print (2+2)
print (12-2)
print (2*2)
print (2/13) #las divisiones siempre darán como resultado un float, con o sin decimal
numero = 32
print (numero)

#limitantes de python
#no está permitido la suma de letras y números
#print ("texto"+13) TypeError: can only concatenate str (not "int") to str

#INTERPOLACIÓN
print(f"el numero es {numero}") #la f permite interpretar dentro del print
nombre = "Diego"

print(f"tu nombre es {nombre} y tienes {numero} años")

#string.format
print("Tu nombre es {} y tu edad es {}".format(nombre,numero))

# formato con %: %s para string y %d para numeros
print("Tu nombre es %s y tu edad es %d" % (nombre,numero))

#metodo con cadena /title hace que la primera letra de las palabras sea mayúscula y las demás minúscula
apellido ="larenas dintrans"
print(apellido.title())