'''
Complexidade Computacional
Lista com 2 milhões de telefones aleatórios
'''
import random

def gera_telefone():
    
    numero_telefone= ''

    for i in range(9):
        if len(numero_telefone) == 4:
            numero_telefone += '-'
        else:
            numero_telefone += str(random.randint(0, 9))

    return numero_telefone

lista_telefonica = {}

arq_nomes = open('nomes.txt', 'r')
nomes = arq_nomes.readlines()

for index in range(len(nomes)):
    nomes[index] = nomes[index].rstrip('\n')

for i in range(2000000):
    nome = nomes[random.randint(0, len(nomes)-1)]
    telefone = gera_telefone()
    lista_telefonica[nome] = telefone
    print('{} nome(s) gerados.'.format(i))

arq_lista_telefone = open('lista_telefones.txt', 'w')

for contato in lista_telefonica:
    str_contato = ''
    str_contato += contato + ' => ' + lista_telefonica[contato] + '\n'
    arq_lista_telefone.write(str_contato)

arq_lista_telefone.close()
                          


