""" 
def imprimir_menu():
    print("Opciones")
    print("1) De acuerdo")  #si no llamamos a la función es un código muerto y no sirve de nada. Simplemente escribirla no genera nada, 
    print("2) En desacuerdo") #luego de defirnirla hay que hacer un llamado o invocación
    print("3) No me interesa")
    
#llamado o invocación, función sin def solo después de haberla definido
imprimir_menu() 
"""
def imprimir_menu():
    print("Opciones")
    print("1) De acuerdo")  
    print("2) En desacuerdo") 
    print("3) No me interesa")

def imprimir_respuestas():
    for i in range(len(respuestas)):
        print(f"La respuesta a la Pregunta nro.{i+1} fue {respuestas[i]} ")

preguntas=["Pregunta nro.1","Pregunta nro.2", "Pregunta nro.3"]
respuestas=[]

for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input("Su respuesta --> "))
    
imprimir_respuestas()
    


"""    
print(f"La respuesta a la primera pregunta fue {respuestas[0]} ")
print(f"La respuesta a la segunda pregunta fue {respuestas[1]} ")
print(f"La respuesta a la tercera pregunta fue {respuestas[2]} ")

for respuesta in respuestas:
    print(f"La respuesta a la {pregunta} fue {respuesta} ")
    


"""