def soma_matrizes(matriz_a, matriz_b):
    '''recebe duas matrizes e retorna a matriz soma, se as matrizes forem de tamanhos diferente retorna erro'''
    if dimensao_matriz(matriz_a) == dimensao_matriz(matriz_b):
        matriz_soma = []
        total_linhas = dimensao_matriz(matriz_a)[0]
        total_colunas = dimensao_matriz(matriz_a)[1]
        for i in range(total_linhas):
            linha_soma = []
            for j in range(total_colunas):
                linha_soma.append(0)
            matriz_soma.append(linha_soma)

        for i in range(total_linhas):
            for j in range(total_colunas):
                matriz_soma[i][j] = matriz_a[i][j] + matriz_b[i][j]
                
        return matriz_soma
    else:
        return False

def dimensao_matriz(matriz):
    '''recebe uma matriz e retorna o tamanho'''
    total_linhas = len(matriz)
    total_colunas = len(matriz[0])
    return [total_linhas, total_colunas]

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))
