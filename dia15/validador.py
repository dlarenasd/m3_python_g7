
def validate(opciones, eleccion):
    """Script para validar la elección de alternativa del usuario

    Args:
        opciones (lista): Lista que contiene las respuestas disponibles
        eleccion (str): letra o número capturado por input 

    Returns:
        str: Luego de verificar que la opción está dentro de las opciones, entrega la opción del usuario
    """
    
    while eleccion not in opciones:
        print("Opción no valida, ingrese una de las opciones válidas")
        eleccion = input('Ingresa una Opción: ').lower()
    # Definir validación de eleccion
    ##########################################################################
    pass
    
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
    
    
