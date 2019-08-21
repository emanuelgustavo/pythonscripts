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
            linha.append(valor)

        #adiciona linha na matriz
        matriz.append(linha)

    return matriz
