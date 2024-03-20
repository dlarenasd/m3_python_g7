import sys, time

#argumento es el dato que ingresa el usuario sin una solicitud de por medio
print(sys.argv)
i = int(sys.argv[1])

while i > 0: 
    print(f"El valor de i  es {i}")
    time.sleep(1)
    i-=1
print("¡BOOOM!")   