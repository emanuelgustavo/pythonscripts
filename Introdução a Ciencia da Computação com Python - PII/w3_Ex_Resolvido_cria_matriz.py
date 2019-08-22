import random as r

def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) => matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas e num_colunas
    colunas em que cada elemento é igual ao valor dado
    '''
    matriz = [] #lista vazia
    for i in range(num_linhas):
        #cria a linha da matriz
        linha = []
        for j in range(num_colunas):
            if valor == '':
                linha.append(r.randint(0,100))
            else:
                linha.append(valor)
    
        #adiciona linha na matriz
        matriz.append(linha)
    
    return matriz
    
def info_matriz():
    linhas = int(input('Digite a quantidade de linhas da matriz: '))
    colunas = int(input('Digite a quantidade de colunas da matriz: '))
    valor = input('Digite o valor da matriz ou enter para aleatorio: ')

    if valor == '':
        matriz = cria_matriz(linhas, colunas, valor)
    else:
        matriz = cria_matriz(linhas, colunas, int(valor))
    
    return matriz
    
print(info_matriz())
