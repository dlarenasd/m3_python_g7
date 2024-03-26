""" 
SETS
Son un conjunto de datos que no permite duplicados
no es ordenado, se escriben con llave
"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
#{'Hurón', 'Hamster', 'Perro', 'Tortuga', 'Gato', 'Erizo de Tierra'}
for animales in muchos_animales:
    print(animales)
    

muchos_animales.add("Chancho")
print(muchos_animales)
#{'Perro', 'Gato', 'Hamster', 'Chancho', 'Erizo de Tierra', 'Hurón', 'Tortuga'} A LOS SETS NO LES IMPORTA EL ORDEN, PONE CUALQUIER ORDEN
muchos_animales.remove("Chancho")
print(muchos_animales)
#{'Tortuga', 'Perro', 'Hurón', 'Hamster', 'Erizo de Tierra', 'Gato'} REMOVE QUITA LAS CLAVES QUE EXISTEN 
muchos_animales.discard("Leon") #{'Perro', 'Gato', 'Erizo de Tierra', 'Hamster', 'Hurón', 'Tortuga'} Puedo pedirle que quite algo que no está y no se cae
print(muchos_animales)

muchos_animales.pop() #Elimina un elemento al azar
print(muchos_animales) #{'Gato', 'Perro', 'Erizo de Tierra', 'Hamster', 'Hurón'}

muchos_animales.clear() #quita todos los elementos del set
print(muchos_animales) #set()

print(muchos_animales.__dir__())
print(muchos_animales)