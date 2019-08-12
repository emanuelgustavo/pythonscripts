def imprime_matriz(matriz):
    '''recebe uma matriz e imprime como matriz'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if j < colunas-1:
                print(matriz[i][j], end=' ')
            else:
                print(matriz[i][j], end='')                
        if i < linhas:
            print()
            
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
    
