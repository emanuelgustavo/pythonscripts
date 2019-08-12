def sao_multiplicaveis(matriz_a, matriz_b):
    '''recebe duas matrizes e verifica se é possivel multiplicá-las, retornando True or False'''
    colunas_matriz_a = len(matriz_a[0])
    linhas_matriz_b = len(matriz_b)
    if colunas_matriz_a == linhas_matriz_b:
        return True
    else:
        return False
'''
m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
print(sao_multiplicaveis(m1, m2))
'''
