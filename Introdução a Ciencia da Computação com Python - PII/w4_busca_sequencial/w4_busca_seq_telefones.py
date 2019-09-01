'''
Complexidade Computacional
Lista com 2 milhões de telefones aleatórios
'''
import random

def busca_contato(nome):
    arq_lista = open('lista_telefones.txt', 'r')
    lista_telefones = arq_lista.readlines()
    lista_contatos = {}
    for linha in lista_telefones:
        contato = []
        contato = linha.split()
        lista_contatos[contato[0]] = contato[1]

    for contato in lista_contatos:
        if contato == nome:
            return [ contato, lista_contatos[contato] ]
        else:
            return print('nenhum contato com esse nome')
        
def gera_nome(lista_nomes):
    
    nome = ''
    
    for i in range(3):
        nome += lista_nomes[random.randint(0, len(lista_nomes)-1)]
        if i < 3:
            nome += ' '
    
    return nome

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

i_quantidade_contatos = 1

while i_quantidade_contatos <= 200000:
    
    nome = ''
    nome = gera_nome(nomes)
    telefone = gera_telefone()
    lista_telefonica[nome] = telefone
    print('{} nome(s) gerados.'.format(i_quantidade_contatos))
    i_quantidade_contatos += 1

print(len(lista_telefonica))

arq_lista_telefone = open('lista_telefones.txt', 'w')

cont = 1
for contato in lista_telefonica:
    #print(cont, contato, sep=' ')
    cont += 1
    str_contato = ''
    str_contato += contato + ' ' + lista_telefonica[contato] + '\n'
    arq_lista_telefone.write(str_contato)

arq_lista_telefone.close()
                          


