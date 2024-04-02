import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    """función de selección de preguntas

    Args:
        dificultad (str): string que contiene el nivel de dificultad de la pregunta

    Returns:
        tupla: retorna un par que contiene como primer elemento un string con el enunciado de la pregunta 
        y un segundo elemento que es la lista de alternativas de la pregunta.
    """
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]  
    # usar opciones desde ambiente global
    global opciones
    opciones_disponibles=opciones[dificultad]
    # escoger una pregunta
    n_elegido = random.choice(opciones_disponibles)
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # escoger enunciado y alternativas mezcladas
    pregunta = preguntas['pregunta_'+str(n_elegido)]
    alternativas = shuffle_alt(pregunta)
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    