def captura_datos():
    """Capturar los números ingresados

    Returns:
        Tupla: Par de números capturados
    """
    x=float(input("Ingrese el primer número: "))
    y=float(input("Ingrese el segundo número: "))
    return x, y 
if __name__=="__main__": #prueba unitaria del código
    print("Probando el metodo captura_datos")
    print(captura_datos())