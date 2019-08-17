def imprime_tabuleiro():
    divisao_horizontal = '+---+---+---+---+---+---+---+---+'
    matriz_tabuleiro = []
    
    for i in range(17):
        linha_tabuleiro = []
        if i % 2 != 0:
            for j in range(33):
                if divisao_horizontal[j] == '+':
                    linha_tabuleiro.append('|')
                elif divisao_horizontal[j]=='-':
                    linha_tabuleiro.append(' ')
        else:
            for j in divisao_horizontal:
                linha_tabuleiro.append(j)
        matriz_tabuleiro.append(linha_tabuleiro)
        
    for i in range(len(matriz_tabuleiro)):
        #print(len(matriz_tabuleiro[i]))
        for j in range(len(matriz_tabuleiro[0])):
            print(matriz_tabuleiro[i][j], end='')
        print()

imprime_tabuleiro()
                