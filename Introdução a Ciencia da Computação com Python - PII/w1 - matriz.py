def cria_matriz(num_linhas, num_colunas):
    '''cria uma matriz com x número de linhas e colunas informados pelo usuário'''
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(str(i)+str(j))
        matriz.append(linha)
        
    return matriz

linhas = int(input('Digite o numero de linhas: '))
colunas = int(input('Digite o numero de colunas: '))
print(cria_matriz(linhas, colunas))
