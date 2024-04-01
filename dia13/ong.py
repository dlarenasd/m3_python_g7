
def fact_i(numero):
    factorial = 1
    for i in range(numero):
        factorial=(factorial*(i+1))
    return factorial

def prod_i(lista):
    productoria = 1
    for i in range(len(lista)):
        productoria = productoria * lista[i]
    return productoria

def calcular(**elementos):
    for clave,valor in elementos.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {fact_i(valor)}")
        elif "prod" in clave:
            print(f"La productoria de {valor} es {prod_i(valor)}")

calcular(fact_1 = 5, prod_1=[4,6,7,4,3], fact_2=6)
