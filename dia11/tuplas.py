""" 
TUPLAS
Son un conjunto de datos ordenados e inmutables
se escriben siempre con paréntesis()
"""

tupla1=(1,3,5,7,9)
print(tupla1)
print(type(tupla1))#tuple o tupla

tupla2=("Nombre","Diego")

nom, texto = tupla2 #-->Nombre va a asociarse a nom y Diego a texto
print(nom) #Nombre
print(texto) #Diego

print(tupla2[0]) #-->Nombre
print(tupla2[1]) #-->Diego
#tupla2[2]="Hola" TypeError: 'tuple' object does not support item assignment -->LAS TUPLAS NO SE PUEDEN MODIFICAR, ni asignar un nuevo dato
#print(tupla2[2]) -->IndexError: tuple index out of range
#tupla2[1]="Hola" --> TypeError: 'tuple' object does not support item assignment, ni tampoco modificar un dato existente

for num in tupla1: #-->recorre los datos de la tupla
    print(num)
    
    
list_dicc1=list({"nota1":5,
    "nota2":6,}.items()) #-->si quiero transformar un diccionario a una lista, se le agrega un .items y todo eso lo agrego adentro de un list()
print(list_dicc1) #dict_items([('nota1', 5), ('nota2', 6)])
print(list_dicc1[0]) #TypeError: 'dict_items' object is not subscriptable/// ('nota1', 5)

print(list_dicc1[0][0])
print(list_dicc1[0][1])
print(list_dicc1[1][0])
print(list_dicc1[1][1])