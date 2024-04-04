import requests
import json

url = "https://reqres.in/api/users?"

payload = json.dumps({
  "first_name": "Ignacio",
  "last_name": "Ramos",
  "job": "profesor",
  "avatar": "https://reqres.in/img/faces/6-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

created_user = response.text
print(created_user)