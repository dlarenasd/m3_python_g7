def sumar(x,y):
    """Imprimir la suma de dos números (x e y)

    Args:
        x (float): primer número
        y (float): segundo número
    """
    print(f"El resultado de la suma es {x+y}")
    
if __name__=="__main__": #prueba unitaria del código
    print("Probando el metodo sumar")
    sumar(4,6)