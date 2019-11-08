import itertools
import time
import random

def converte_string_senha(numeros):
    senha = ''
    for x in numeros:
        senha += str(x)
    return senha

def descobre_senha(senha):
    for p in itertools.permutations('0123456789'):
        teste = converte_string_senha(p)
        if teste == senha:
            return True
    return False

start = time.time()

#for p in itertools.permutations('ABCD'):
#    print(p)
    
numeros = [random.randint(0,10) for x in range(9)]

senha = converte_string_senha(numeros)

print(senha)

descobriu = False

while not descobriu:
    descobriu = descobre_senha(senha)

end = time.time()
print('Tempo gasto para descobrir os números: {}s'.format(end-start))
    

