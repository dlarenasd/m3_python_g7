import requests
import json

url = "https://reqres.in/api/users/5"

payload = json.dumps({
            "id": 5,
            "residence": "zion",
            "first_name": "morpheus",
            "last_name": "Ramos",
            "avatar": "https://reqres.in/img/faces/5-image.jpg"
        
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

#print(response.text)
updated_user = response.text
print(updated_user)