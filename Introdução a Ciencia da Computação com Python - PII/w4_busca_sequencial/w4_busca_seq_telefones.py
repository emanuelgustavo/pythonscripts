'''
Complexidade Computacional
Lista com 2 milhões de telefones aleatórios
'''
import random

def main():
    
    #gera_lista_telefonica()
    nome_busca = input('Digite o nome a buscar na lista: ')
    lista_telefonica = carrega_contatos()
    print(busca_contato(nome_busca, lista_telefonica))


def carrega_contatos():
    
    matriz_lista_telefonica = []
    
    with open('lista_telefones.txt', 'r') as arq_lista_telefone:
        lista_contatos = arq_lista_telefone.readlines()
        
        for linha in lista_contatos:
            linha_matriz = []
            numero, nome, telefone = linha.split(';')
            linha_matriz.append(numero)
            linha_matriz.append(nome)
            linha_matriz.append(telefone)
            matriz_lista_telefonica.append(linha_matriz)
    
    return matriz_lista_telefonica
            
def busca_contato(nome, lista_contatos):
    
    for contato in lista_contatos:
        if nome.lower() == contato[1].lower():
            return contato
        print('Nenhum contato com esse nome')
        
def gera_nome(lista_nomes):
    '''função gera e retorna um nome aleatoriamente como string'''
    return lista_nomes[random.randint(0, len(lista_nomes)-1)]
    
def gera_telefone():
    '''função gera e retorna um numero de 8 digitos aleatoriamente como string'''
    
    numero_telefone= ''

    for i in range(9):
        if len(numero_telefone) == 4:
            numero_telefone += '-'
        else:
            numero_telefone += str(random.randint(0, 9))

    return numero_telefone

def gera_lista_telefonica():

    lista_telefonica = []

    arq_nomes = open('nomes.txt', 'r')
    nomes = arq_nomes.readlines()

    for index in range(len(nomes)):
        nomes[index] = nomes[index].rstrip('\n')

    i_quantidade_contatos = 0

    while i_quantidade_contatos <= len(nomes)-1:
        
        contato = []
        nome = nomes[i_quantidade_contatos]
        #nome = gera_nome(nomes)
        telefone = gera_telefone()
        contato.append(nome)
        contato.append(telefone)
        lista_telefonica.append(contato)
        print('{} nome(s) gerados. {}'.format(i_quantidade_contatos, contato))
        i_quantidade_contatos += 1

    print(len(lista_telefonica))

    arq_lista_telefone = open('lista_telefones.txt', 'w')

    cont = 1
    for contato in lista_telefonica:
        #print(cont, contato, sep=' ')
        cont += 1
        str_contato = ''
        str_contato += str(cont) +';' + contato[0] + ';' + contato[1] + '\n'
        arq_lista_telefone.write(str_contato)

    arq_lista_telefone.close()
    
main()
                          


