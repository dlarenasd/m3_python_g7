import requests

url = "https://reqres.in/api/users/6"

payload = {}
headers = {}

response = requests.request("DELETE", url)

print(response.text)
