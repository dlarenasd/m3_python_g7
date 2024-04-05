from string import Template
def html_template():
    """función para elaborar un Template de HTML

    Returns:
        str: HTML escrito como string listo para que se le agreguen las cards
    """
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
    ''')#cards = html_template.substitute(cards='xxxx')//incluyo bootstrap para que funcione el html y dejo una estructura en fila para las cards
    return html_template

def cards_template():
    """función para elaborar un Template de card

    Returns:
        str: Card escrita como string lista para que se le agreguen la URL y los textos en español e inglés. 
        Adicionalmente tiene un div para que se comporten como columna y sean responsivas.
    """
    card_template = Template("""<div class="col-12, col-lg-4">
            <div class="card">
                <img src="$url" class="card-img-top" alt="$txt_es">
                <div class="card-body">
                    <p class="card-text fs-4 fw-bold">$txt_es</p>
                    <p class="card-text fs-4 fw-bold">$txt_en</p>
                </div>
            </div>
        </div>""") #card_template.substitute(url="xxxxxxx", txt_es="xxxxxxx", txt_en="xxxxxxx") // les dejo un div de columna para que cada card se comporte como columna 
    return card_template
