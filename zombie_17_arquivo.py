arquivo = open('numeros.txt', 'w')
for linha in range(100):
    arquivo.write('%s \n' % linha)
arquivo.close()
