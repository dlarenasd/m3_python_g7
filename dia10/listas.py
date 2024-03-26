from os import system
""" 
LISTAS ---> []

()-->tuplas
{}-->diccionarios

son contenedores de datos
son mutables

los elementos de la lista serán todo lo que esté entro de los corchetes y separados por coma

conjunto de datos, separados por coma y ordenados según su ingreso
el índice o posición va desde el 0 a n-1

"""

lista_pares = [2, 4, 6, 8, 10]
#tamaño de la lista es 5, cuántos elementos tiene
print(len(lista_pares)) #-->imprime el tamaño o el largo de la lista
print(lista_pares) #al imprimirlos se ven con corchete

print(lista_pares[0]) #imprimir un elemento específico de la lista ingresando su índice-->2
print(lista_pares[1])#-->4
print(lista_pares[2])#-->6 además al imprimir un elemento específico lo hace sin los corchetes
print(lista_pares[3])#-->8
print(lista_pares[4])#-->10
#print(lista_pares[5]) error: el índice está fuera de rango
print("")
print(lista_pares[-1]) #-->último elemento de la lista
print(lista_pares[-2])#penúltimo elemento de la lista

lista_vacia =[]

#MÉTODOS
print(lista_pares.__dir__) #<built-in method __dir__ of list object at 0x0000012B4931D900> -->representación de un objeto, un espacio de memoria
"""print(lista_pares.__dir__())
['__new__', '__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__init__', '__len__', '__getitem__', '__setitem__', '__delitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__iadd__', '__imul__', '__reversed__', '__sizeof__', 'clear', 'copy', 'append', 'insert', 'extend', 'pop', 'remove', 'index', 'count', 'reverse', 'sort', '__class_getitem__', '__doc__', '__str__', 
'__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__dir__', '__class__']"""
#append(dato)-->agregar un elemento al final de la lista
print("")
lista_vacia.append("Lunes")
print(lista_vacia)
#append al ser un método que pone un dato al final, se recomienda usarlo incluyendo datos de a uno
lista_vacia.append("Martes")
lista_vacia.append("Miércoles")
lista_vacia.append("Jueves")
lista_vacia.append("Viernes")
lista_vacia.append("Sábado")
lista_vacia.append("Domingo") #el método es el que se encarga de dejar el elemento en la posición, SIEMPRE AL FINAL
print(lista_vacia)

#INSERT (indice, elemento)
lista_vacia.insert(4,"al fin Viernes") #agrega en la pósición 4 ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'al fin Viernes', 'Viernes', 'Sábado', 'Domingo']
lista_vacia.insert(4,"San Jueves")#agrega otro elemento en la posición 4 (desplazando los demás elementos hacia el final)
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves', 'San Jueves', 'al fin Viernes', 'Viernes', 'Sábado', 'Domingo']
lista_vacia[4]="Jueves" #reemplazar el elemento de la posición indicada con un elemento ingresado
print(lista_vacia)

lista_vacia.insert(10, "Sabingo") #al incluir un elemento en una posición que no está, lo incluye al final
#lista_vacia[11]="Día extra" IndexError: list assignment index out of range --> NO PUEDES REEMPLAZAR ALGO QUE NO ESTÁ
print(lista_vacia)

system("cls")

#POP es un método para sacar el último elemento de dentro de la lista
eliminados = []
eliminados.append(lista_vacia.pop(4)) #borra el elemento de una posición
print(lista_vacia)
#print(f"el elemento eliminado es {eliminados}")
eliminados.append (lista_vacia.pop(4))
print(lista_vacia)
eliminados.append(lista_vacia.pop()) #borra el elemento del final
print(lista_vacia)
print(eliminados)

system("cls")
#REMOVE (valor)-->elimina un valor

lista_vacia.remove("Domingo")
print(lista_vacia) #['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
#lista_vacia.remove("Domingo") ValueError: list.remove(x): x not in list -->no se puede remover elementos que no están
lista_vacia.append("Sábado")
lista_vacia.remove("Sábado") #elimina la primera coincidencia
print(lista_vacia)

system("cls")
lista_vacia.append("Domingo")
#reverse () --> invierte los elementos de una lista, el cambio es permanente
lista_vacia.reverse()
print(lista_vacia) # ['Domingo', 'Sábado', 'Viernes', 'Jueves', 'Miércoles', 'Martes', 'Lunes']


#SORT --> ordena los elementos de forma ascendente, es permanente
lista_vacia.sort()
print(lista_vacia) #['Domingo', 'Jueves', 'Lunes', 'Martes', 'Miércoles', 'Sábado', 'Viernes'] orden alfabético

lista_pares.reverse()
print(lista_pares) #[10, 8, 6, 4, 2]
lista_pares.sort() 
print(lista_pares) #[2, 4, 6, 8, 10]

print(lista_vacia)
#SIEMPRE QUE TRABAJES CON UNA LISTA, SI LA MODIFICAS SIN RESPALDARLA, VAS A PERDER LA ORIGINAL.
#SE SUGIERE RESPALDARLA EN UN OBJETO SEPARADO

#RESPALDO DE LISTAS

#lista1 = lista_pares --->esto NO SE HACE, NO HACES UNA NUEVA LISTA, SOLO TIENES UNA VARIABLE QUE APUNTA A LOS DATOS DE OTRA VARIABLE
#CUALQUIER CAMBIO EN LISTA PARES SERÍA PARA AMBAS

lista2=lista_pares.copy() #-->así SI SE HACE 
lista3=lista_pares[:] #-->así también
lista4=lista_pares+[] #-->forma no limpia de hacer una copia, medio a la mala
lista5=lista_pares*1#-->forma igual de poco limpia
lista6=list(lista_pares) #-->esta forma si es limpia
lista_pares.append(12)
print(lista_pares)
print(lista2)
print(lista3)

#SORTED (lista, reverse:True(para descendente)) ordena descendentemente pero no es permanente
print(sorted(lista3,reverse=True))

#INDEX lista.index()-->nos retorna el índice de un elemento en la lista
print(lista_pares.index(6))#el índice del elemento 6 en la lista_pares
# print(lista_pares.index(15))-->ValueError: 15 is not in list

lista_final = lista_pares + lista_vacia
print("lista final es", lista_final)
