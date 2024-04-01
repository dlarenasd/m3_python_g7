import sys


def filtrar(diccionario,umbral):
    if len(sys.argv) == 2:
        filtro = {producto:valor for producto,valor in diccionario.items() if valor>umbral}    
    elif len(sys.argv) >2:
        if sys.argv[2].lower()=="mayor":
            filtro = {producto:valor for producto,valor in diccionario.items() if valor>umbral}  
        elif sys.argv[2].lower()=="menor":
            filtro = {producto:valor for producto,valor in diccionario.items() if valor<umbral}    
    return filtro

def lista_productos():
    productos=[]
    filtro = filtrar(precios, int(sys.argv[1]))
    for producto in filtro.keys():
        productos.append(producto)
    return productos

def respuesta():
    if len(sys.argv) ==2:
        productos=lista_productos()
        return (f"Los productos mayores al umbral son: {", ".join(productos)}")
    elif sys.argv[2].lower()=="mayor":
        productos=lista_productos()
        return (f"Los productos mayores al umbral son: {", ".join(productos)}")
    elif sys.argv[2].lower()=="menor":
        productos=lista_productos()
        return (f"Los productos menores al umbral son: {", ".join(productos)}")
    else:
        return "Lo sentimos, no es una operación válida"


precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000}


print(respuesta())