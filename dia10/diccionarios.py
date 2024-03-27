from os import system
""" 
DICCIONARIOS {}
estructura datos de pares (clave:valor)
almacenan una gran cantidd de datos
para poder acceder a un elemento del diccionario, se debe hacer a través de la clave, no importa la posicion
las claves no se generan de manera automática, se debe ser explícito
son elementos NO ORDENADOS
las claves pueden ser string, numérico entero (int) o incluso un Boolean, listas, diccionarios u otro tipo de datos

diccionario[clave]=valor --->si la clave existe, modifico su valor, si no existe la genero

"""
diccionario ={
    1:"uno",
    2:"dos",
    3:"tres",
    "cuatro":4,
    5:["a","b","c"],
    "dicc":{"A":"a mayúscula"}, 
    }

notas={}#-->diccionario vacío
print(len(notas)) #cuál es el tamaño de un diccionario
notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Daniela": 5,
    "Vicente": 7,
    "FELIPE": 3,
    "Vicente": 2,# al duplicar una clave, la clave se va a asociar a su último valor
    }
system("cls")
print(len(notas))#ahora es 5, dado que los elementos son los pares
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#acceso a los elementos de un diccionario (valores del diccionario)
print(notas["Camila"]) #7
print(notas["Antonio"]) #5
print(notas["Daniela"]) #5
print(notas["Felipe"]) #6
print(notas["Vicente"]) #7 -->por la clave duplicada se reeemplaza el 7 por un 2, que es el último dato ingresado con la clave Vicente
#print(notas["felipe"]) --> KeyError: 'felipe' ES SENSIBLE A MAYÚSCULAS, LA CLAVE DEBE SER INGRESADA EXACTAMENTE IGUAL, SON ÚNICAS

#AGREGAR ELEMENTOS A UN DICCIONARIO, sumar un nuevo par-->diccionario[nueva clave]=nuevo valor
print(notas)
notas["Julio"]=4
print(notas)

#MODIFICAR EL PAR clave:valor (lo que se modifica es el valor, no la clave)
notas["Julio"]=5
print(notas)

#ELIMINAR UN PAR clave:valor
del notas["FELIPE"]
print(notas)

#2da forma es con pop(), permite que al eliminar capturemos el valor 
eliminado=notas.pop("Camila")
print(eliminado)
print(notas)

notas2 ={
    "Manuel":2 , 
    "Marcelo":5,
    "Felipe":7,}

#notas.update(notas2)
notas2.update(notas)
print(notas2) #{'Manuel': 2, 'Marcelo': 5, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 2, 'Julio': 5}

#COLISIONES: Al hacer un update, si una clave está repetida, se conserva el valor del diccionario anexado
print(notas2.keys()) #dict_keys(['Manuel', 'Marcelo', 'Felipe', 'Antonio', 'Daniela', 'Vicente', 'Julio'])
print(notas2.values()) #dict_values([2, 5, 6, 5, 5, 2, 5])
print(notas2.items())#dict_items([('Manuel', 2), ('Marcelo', 5), ('Felipe', 6), ('Antonio', 5), ('Daniela', 5), ('Vicente', 2), ('Julio', 5)])
#items entrega una lista de los pares clave:valor en forma de tupla
print(notas2.get("Marcelo")) #5 --> diccionario.get(clave) -->retorna el valor asociado a la clave
print(notas2.get("Pedro")) #None --> Al consultar por una clave no existente, retornará por Default "None"
print(notas2.get("Pedro","Valor no existe"))#Valor no existe -->se puede especificar el valor de retorno al no existir la clave


""" 
transformar una lista en diccionario -->(una lista de tuplas)usando el método .dict()
transformar en tupla-->método .tuple()
transformar en set -->método .set()
"""