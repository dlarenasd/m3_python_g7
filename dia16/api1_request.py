import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {} #datos a enviar
headers = {} #formato o tipo de dato

response = requests.request("GET", url, headers=headers, data=payload)
#repuesta = en la libreria requests, mi petición es que me "obtengas" lo que hay en la siguiente URL

#print(response.text)
print("")
print(response) #<Response [200]>

if response.status_code == 200: #200 da el OK, la petición está buena y estoy pidiendo algo que existe
    #print(response.text) #transforma el reponse en un string en formato JSON
    print(response.json()) #convierte la respuesta en un JSON y nos permite trabajar con ella como lista/diccionario/etc
    respuesta = response.json() #capturamos el contenido en una variable y en este caso podremos trabajar con la estructura de datos
    print("")
    print(respuesta["title"]) #solicito el valor asociado a la clave "title" del diccionario --> sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    for clave,valor in respuesta.items():
        print(f"Clave {clave} - Valor {valor}")
        """ Clave userId - Valor 1
            Clave id - Valor 1
            Clave title - Valor sunt aut facere repellat provident occaecati excepturi optio reprehenderit
            Clave body - Valor quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"""
else:
    print("Error en la solicitud", response.status_code)
