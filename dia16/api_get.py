import requests, json

url = "https://jsonplaceholder.typicode.com/posts"

payload = {} #datos a enviar
headers = {} #formato o tipo de dato

response = requests.get(url)
#respuesta = de la libreria requests quiero obetener lo que hay en la siguiente URL (funciona igual)

#print(response.text)
print("")
print(response) #<Response [200]>

if response.status_code == 200: #200 da el OK, la petición está buena y estoy pidiendo algo que existe
    print(response.text) #transforma el reponse en un string en formato JSON
    respuesta = json.loads(response.text) #de la librería json usamos el método loads() que toma el string, identifica el tipo de objeto y lo transforma de texto a su tipo
    print(type(respuesta)) #<class 'list>
    for posicion, dicc in enumerate(respuesta):
        print(f"Diccionario {dicc} en la posición {posicion}")
    """
    print(type(respuesta)) #<class 'dict'>
    for clave,valor in respuesta.items():
        print(f"Clave: {clave} - Valor: {valor}")
    """

else:
    print("Error en la solicitud", response.status_code)
