def marque_atacadas(tab):
    divisao_horizontal = '+---+---+---+---+---+---+---+---+'
    matriz_tabuleiro = []
    
    posicao_peca = acha_posicao_peca(tab)
    posicao_peca_linha_tabuleiro = posicao_peca[0]
    posicao_peca_coluna_tabuleiro = posicao_peca[1]
    peca_linha = posicao_peca[2]
    peca_coluna = posicao_peca[3]
    
    for i in range(17):
        linha_tabuleiro = []
        if i % 2 != 0:
            for j in range(33):
                if divisao_horizontal[j] == '+':
                    linha_tabuleiro.append('|')
                elif divisao_horizontal[j]=='-':
                    if i == posicao_peca_linha_tabuleiro and j == posicao_peca_coluna_tabuleiro:
                        linha_tabuleiro.append(tab[peca_linha][peca_coluna])
                    else:
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
        
def acha_posicao_peca(tab):
    tabuleiro = tab
    posicao_peca_linha = 0
    posicao_peca_coluna = 0
    
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    
    for i in range(linhas):
        for j in range(colunas):
            if tabuleiro[i][j] != ' ':
                posicao_peca_coluna = j
                posicao_peca_linha = i
        print()
    
    posicao_coluna = {
        0:2,
        1:6,
        2:10,
        3:14,
        4:18,
        5:22,
        6:26,
        7:30
    }
    posicao_Linha = {
        0:1,
        1:3,
        2:5,
        3:7,
        4:9,
        5:11,
        6:13,
        7:15 
    }
                
    return [posicao_Linha[posicao_peca_linha], posicao_coluna[posicao_peca_coluna], posicao_peca_linha, posicao_peca_coluna]
    
    
    
        
tabuleiro = [ list('        '),
              list('        '),
              list('        '),
              list('   R    '),
              list('        '),
              list('        '),
              list('        '),
              list('        ') 
            ]


marque_atacadas(tabuleiro)

              