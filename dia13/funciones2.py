#RETURN
def sumar(numero1,numero2):
    suma=numero1+numero2
    return(suma) #return 29

sumar(14,15)#--->hasta acá no pasa nada, sería solo llamar el 29 sin hacer nada con él

print(sumar(15,16)) #--> esto si funciona, porque pedimos sumar, que almacene el resultado y con el print le pedimos que imprima el valor de retorno

#capturar el valor de retorno
valor_retorno = sumar(16,17)
print(valor_retorno)