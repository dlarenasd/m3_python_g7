from string import Template

img_template = Template('<img src="$url">') #imagen = img_template.substitute(url='xxxxx')
html_template = Template(''' <!DOCTYPE html>
<html>
<head>
<title>Aves de Chile</title>
</head>
<body>
<h1>Aves de Chile</h1>
$body
</body>
</html>
''')