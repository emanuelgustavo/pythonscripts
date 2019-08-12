def dimensoes(matriz):
    total_linhas = len(matriz)
    total_colunas = len(matriz[0])
    print('{}X{}'.format(total_linhas, total_colunas))

dimensoes([[1, 2], [3, 4]])

dimensoes([[1, 1], [1, 1]])

dimensoes([[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1], [2, 3, 6, 7]])

dimensoes([[1, 2, 7, 1], [3, 4, 8, 1], [1, 2, 3, 1]])

dimensoes([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])

dimensoes([[1], [2]])

dimensoes([[1, 2]])

dimensoes([[1]])
