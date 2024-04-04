import requests
import json 
from string import Template

def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get("https://aves.ninjas.cl/api/birds")
img_template = Template('<img src="$url">')
#print(len(response)) --->216
#print(type(response)) ---><class 'list'>
#print(response[0])

lista_url_fotos = []
nombre_spanish = []
nombre_english = []
for diccionario in response:
    lista_url_fotos.append(diccionario['images']['main'])
    nombre_spanish.append(diccionario['name']['spanish'])
    nombre_english.append(diccionario['name']['english'])

texto_img = ''
for url in lista_url_fotos:
    texto_img += img_template.substitute(url=url) +'\n'
print(texto_img)
