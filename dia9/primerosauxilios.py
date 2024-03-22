import sys
print("Este bot es para guiarte frente a primeros auxilios, tendrás que responder con S y N (como si y no) para responder a las preguntas")

print("¿La persona responde a estímulos?")
respuesta = input("¿Si o No?").upper()
if respuesta == "N":
    print("Abrir la vía aérea")
    print("¿Respira?")
    respuesta = input("¿Si o No?").upper()
    if respuesta == "N":
        print("Administra 5 ventilaciones y llama a una ambulancia")
        while respuesta == "N":
            print("¿Tiene signos vitales?")
            respuesta = input("¿Si o No?").upper()
            if respuesta == "N":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")
            else:
                print("Reevaluar a la espera de la ambulancia")
                print("¿Llegó la ambulancia?")
                respuesta = input("¿Si o No?").upper()
                if respuesta == "S":
                    break
    else:
        print("Permitirle posición de suficiente ventilación")
else:
    print("Valorar la necesidad de llevarlo al hospital más cercano")