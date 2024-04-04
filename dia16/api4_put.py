import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {     # modifica/actualiza el diccionario que estamos ingresando con los datos que pongamos
    "userId": 1,
    "title": "título de ejemplo 2",
    "body": "esto es un mejor ejemplo de body"
}

response = requests.put(url, json=payload)

if response.status_code == 200: 
    print("Actualización exitosa")
    print(response.text)
else: 
    print("Error en la actualización de posts")

