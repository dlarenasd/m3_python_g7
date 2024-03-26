""" 
-crear un diccionario
-agregar un elemento
-modificar un elemento
-eliminar un elemento
"""

personajes = {"Kaladin":"Pobre tipo"}
print(personajes)
personajes["Adolin"]="Insufrible"
print(personajes)
personajes["Adolin"]="Qué buen tipo"
print(personajes)
del personajes["Kaladin"]
print(personajes)