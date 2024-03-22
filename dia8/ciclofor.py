#CICLO FOR
# for VARIABLE in ITERABLE:

#[0, 1, 2 ,3, 4, 5, 6, 7, 8, 9] el valor de un range nunca va a ser coniderado, parte siempre con 0 por default.
for i in range(10): 
    print(i)

print("")
#[4,5,6,7,8,9] definir un valor de inicio que es considerado y un valor de fin que no es considerado
for i in range(4,10): 
    print(i)

print("")
#[4,6,8] 4 es valor de inicio, 10 es valor de término (no considerado) y 2 es el incremento
for i in range(4,10,2): 
    print(i)
    
""" 
FOR EN JAVASCRIPT
for (let index = 4; index < 10; index++) {
    console.log(index);
}
"""
print("")
#LISTAS
numeros=[2,"4",True,3,"5"]
for numero in numeros:
    print(numero)
    
print("")

#   String
texto = "Hola Mundo"
for caracter in texto:
    print(caracter) #los string son similares a las listas

#EL CICLO FOR PERMITE PONERLE CUALQUIER NOMBRE A LA VARIABLE ITERADORA, DEBE REPRESENTAR EL ELEMENTO SINGULAR DE LA VARIABLE PLURAL

print("")
#DICCIONARIO clave:valor
datos_personales = {
    "nombre" : "Diego",
    "apellido": "Larenas",
    "edad": 32
}
for clave in datos_personales:  #IMPRIME LAS CLAVES
    print(clave)
    
print("")

for clave in datos_personales:  #IMPRIME LOS VALORES
    print(datos_personales[clave])
    
print("")

for clave,valor in datos_personales.items():  #IMPRIME CLAVE,VALOR
    print(f"clave: {clave} - valor:{valor}")

print("")

for par in datos_personales.items():  #IMPRIME CLAVE,VALOR
    print(par)
    
print("")

for clave in datos_personales.keys():  #clave
    print(clave)
    
for valor in datos_personales.values():  #valor
    print(valor)
    
print("")

#ENUMERATE 
texto = "Esternocleidooccipitomastoideo"
for posicion, caracter in enumerate (texto):
    print(f"la posición {posicion} del caracter {caracter}")

print("")

for posicion, numero in enumerate (numeros):
    print(f"la posición {posicion} del caracter {numero}")
    
print("")

prefijo = ['La','El','La','El']
frutas = ['manzana', 'platano','frutilla','tomate']
colores = ['verde','amarillo','roja','rojo']
for p, fruta, color in zip(prefijo, frutas, colores):
    print(f'{p} {fruta} es de color {color}') #Procesa varias listas en una misma iteración, haciendo corresponder sus posiciones
    

print("")

numeros=[2,"4",True,3,"5",[2,5,8],{"clave":"valor"}]
for numero in numeros:
    print(numero)
    if numero == 3:
        break
print("fuera del for")

print("")
