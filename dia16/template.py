from string import Template

img_template = Template('<img src="$url">') #imagen = img_template.substitute(url='xxxxx')
html_template = Template(''' <!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')