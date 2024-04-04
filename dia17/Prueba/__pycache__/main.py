import requests
import json 
import template
def request_get(url):
    """Función para obtener información de una API

    Args:
        url (str): URL de acceso a la API

    Returns:
        _type_: Dependiendo del contenido de la API puede retornar un diccionario, lista, tupla ya en formato.
    """
    return json.loads(requests.get(url).text)

response = request_get("https://aves.ninjas.cl/api/birds") #solicito el contenido de la API con la función

#print(len(response)) --->tiene 216 elementos
#print(type(response)) ---><class 'list'>
#print(response[0]) -->{'uid': '76-buteo-albigula', 'name': {'spanish': 'Aguilucho Chico', 'english': 'White-throated Hawk', 'latin': 'Buteo albigula'}, 'images': {'main': 'https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.200x0.jpg', 'full': 'https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.jpg', 'thumb': 'https://aves.ninjas.cl/api/site/assets/files/3099/17082018024245aguilucho_chico_tomas_rivas_web.200x0.jpg'}, '_links': {'self': 'https://aves.ninjas.cl/api/birds/76-buteo-albigula', 'parent': 'https://aves.ninjas.cl/api/birds'}, 'sort': 0}
#cada elemento de la lista response es un diccionario
lista_url_fotos = []
nombre_es = []
nombre_en = []
for diccionario in response: #recorro cada diccionario de la lista obtenida
    lista_url_fotos.append(diccionario['images']['main']) #e incluyo en una lista las URL de las fotos
    nombre_es.append(diccionario['name']['spanish']) #también armo una lista para los nombres en español
    nombre_en.append(diccionario['name']['english']) #y una lista para los nombres en inglés

card_template = template.cards_template() #hago una variable que contenga el módulo para usar los template de cards(si no lo hago no puedo usar el substitute)
cards=""    #Hago un string vacío para luego rellenarlo
for foto, nom_es, nom_en in zip(lista_url_fotos,nombre_es,nombre_en): #asocio en tríos url, nombre en español y nombre en inglés y los recorro
    
    cards += card_template.substitute(url=foto, txt_es=nom_es, txt_en=nom_en)+"\n"  #y relleno a continuación el string vacío con las 216 iteraciones/tríos en forma de card
    
html_template = template.html_template() #asocio una variable al template obtenido por función
html = html_template.substitute(cards = cards) #sustituyo en el template y relleno con la variable cards que contiene las 216 cards
#print(html)

with open('dia17/Prueba/index.html', 'w') as file:  #abro un archivo de nombre index.html en modo de escritura y lo relleno con el html recién hecho, luego lo exporto
    file.write(html)





    