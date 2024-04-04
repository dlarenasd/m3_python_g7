import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = json.dumps({
  "userId": 1,
  "title": "título de ejemplo",
  "body": "esto es un mejor ejemplo de body"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

