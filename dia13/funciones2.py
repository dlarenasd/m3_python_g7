#RETURN
def sumar(numero1,numero2):
    suma=numero1+numero2
    return(suma) #return 29 --->en el retorno podría haber hecho la operatoria sin definir ninguna variable 
    
""" 
def sumar(numero1,numero2):
    return numero1+numero2
"""
sumar(14,15)#--->hasta acá no pasa nada, sería solo llamar el 29 sin hacer nada con él

print(sumar(15,16)) #--> imprimir el valor de retorno

#capturar el valor de retorno al llamar la función
valor_retorno = sumar(16,17) #-->valor_retorno = 33
print(valor_retorno)


def cuadrado_cubo(base):
    cuadrado = base**2
    cubo = base**3
    return cuadrado, cubo

print(cuadrado_cubo(2))#(4,8)

valor_cuadrado, valor_cubo = cuadrado_cubo(2)
print(valor_cuadrado) #4
print(valor_cubo) #8