import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

payload = json.dumps({     #json.dumps() agrega el diccionario que estamos ingresando y le agrega un id
    "userId": 1,
    "title": "título de ejemplo",
    "body": "esto es un ejemplo de body"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
