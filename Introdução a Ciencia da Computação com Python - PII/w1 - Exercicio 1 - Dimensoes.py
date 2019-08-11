def dimensoes(matriz):
    total_linhas = len(matriz)
    total_colunas = len(matriz[0])
    '''
    for linha in matriz:
        for coluna in linha:
            total_colunas += 1
        total_linhas += 1
    '''
    return '{}x{}'.format(total_linhas, total_colunas)
