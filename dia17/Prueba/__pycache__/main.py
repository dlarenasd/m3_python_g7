import requests
import json 
from string import Template

def request_get(url):
    """Función para obtener información de una API

    Args:
        url (str): URL de acceso a la API

    Returns:
        _type_: Dependiendo del contenido de la API puede retornar un diccionario, lista, tupla ya en formato.
    """
    return json.loads(requests.get(url).text)

response = request_get("https://aves.ninjas.cl/api/birds")
#img_template = Template('<img src="$url">')
#print(len(response)) --->216
#print(type(response)) ---><class 'list'>
#print(response[0])
html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Aves de Chile</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body>
<h1 class="text-center">Aves de Chile</h1>
<div class="container">
    <div class="row gx-3 gy-3">
            $cards
    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
''')
card_template = Template("""<div class="col-10, col-md-4">
            <div class="card" style="width: 18em;">
                <img src="$url" class="card-img-top" alt="$txt_es">
                <div class="card-body">
                    <p class="card-text">$txt_es</p>
                    <p class="card-text">$txt_en</p>
                </div>
            </div>
        </div>""") 

lista_url_fotos = []
nombre_es = []
nombre_en = []
for diccionario in response:
    lista_url_fotos.append(diccionario['images']['main'])
    nombre_es.append(diccionario['name']['spanish'])
    nombre_en.append(diccionario['name']['english'])
    
cards=""    
for foto, nom_es, nom_en in zip(lista_url_fotos,nombre_es,nombre_en):
    
    cards += card_template.substitute(url=foto, txt_es=nom_es, txt_en=nom_en)+"\n"
    

html = html_template.substitute(cards = cards)
print(html)

with open('output.html', 'w') as file:
    file.write(html)





    