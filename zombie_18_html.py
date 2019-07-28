'''
arquivo html
'''
arquivo = open('ola.html', 'w', encoding='utf-8')
arquivo.write('''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Teste</title>
</head>
<body>
<p>Olá Mundo!</p>
</body>
</html>''')
arquivo.close()
 
