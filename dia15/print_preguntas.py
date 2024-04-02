import preguntas as p

def print_pregunta(enunciado, alternativas):
    """función de impresión de enunciado y alternativas de una pregunta

    Args:
        enunciado (str): String de texto con el enunciado de una pregunta
        alternativas (list): lista de alternativas de una pregunta
    """
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado[0])
        
    for opcion, alternativa in zip(["A.","B.","C.","D."],alternativas):
        print(opcion,alternativa[0])
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4