def restar(x,y):
    """Imprimir la resta de dos números (x e y)

    Args:
        x (float): primer número
        y (float): segundo número
    """
    print(f"El resultado de la resta es {x-y}")

if __name__=="__main__": #prueba unitaria del código
    print("Probando el metodo restar")
    restar(4,6)