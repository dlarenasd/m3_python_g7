def choose_level(n_pregunta, p_level):
    """Elegir un nivel de dificultad

    Args:
        n_pregunta (int): número de la pregunta
        p_level (str): número de preguntas por nivel de dificultad

    Returns:
        str: string que señala el nivel de dificultad escogido
    """
            
            
    # Construir lógica para escoger el nivel
    ##################################################
    if n_pregunta <= p_level:
        level = 'basicas'
    elif n_pregunta > p_level and n_pregunta <=2*p_level:
        level = 'intermedias'
    elif n_pregunta > 2*p_level and n_pregunta <=3*p_level:
        level = 'avanzadas'   
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 3)) # avanzadas
    print(choose_level(4, 3)) # intermedias