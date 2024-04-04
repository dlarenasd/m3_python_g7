import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {     # agrega el diccionario que estamos ingresando y le agrega un id
    "userId": 1,
    "title": "título de ejemplo",
    "body": "esto es un ejemplo de body"
}

response = requests.post(url, json=payload)

if response.status_code == 201: #201 lo entrega postman al crear un elemento
    print("Inserción exitosa")
    print(response.text)
else: 
    print("Error en la creación de posts")

