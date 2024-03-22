#10 PRIMEROS PARES

n = 10
lista_pares =[] # lista vacía, de tamaño 0
for i in range (n):
    lista_pares.append(2*(i+1)) #[2,4,6,8,10,12,14,16,18,20]

print(lista_pares)

#COMPREHENSION [formula for variable in range()]

lista_pares2 = [2*(i+1) for i in range (n)]
print(lista_pares2)

print("")
valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
print(divisibles)

#[expresión1 if condición1 else expresión2 for variable in iterable]
divisibles2 = ["Divisible" if valor%2 == 0 else "No Divisible" for valor in valores]
print(divisibles2)


print("")

#FILTRADO   
lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
lista_str = []
lista_int = []
lista_float= []
lista_bool=[]
count_str = 0
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
    elif type(elemento) is float:
        count_str += 1
        lista_float.append(elemento)
    elif type(elemento) is int:
        count_str += 1
        lista_int.append(elemento)
    if type(elemento) is bool:
        count_str += 1
        lista_bool.append(elemento)
print(count_str)
print(lista_str) 
print(lista_int)
print(lista_float)
print(lista_bool)

print("")

lst_str = [elemento for elemento in lista if type(elemento) is str ]
print(len(lst_str))
print(lst_str)


#DICTIONARY COMPREHENSION
claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = {k:v for k,v in zip(claves, valores)}
print(diccionario2)

