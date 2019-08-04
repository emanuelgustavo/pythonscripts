def computador_escolhe_jogada(n, m):

    #print('É a vez do computador!')
    #print('Peças em jogo: {} | Peças permitidas retirar na rodada: {}'.format(n, m))

    if n <= m:

        print('O computador retirou: {}'.format(n if n > 1 else 'uma'))
        return n

    elif n > m:
        
        x = 1

        while x < m:
            
            testex = n
            testex -= x

            if testex % (m + 1) == 0:

                break

            x += 1

        print('O computador retirou: {}'.format(x))
        return x


def usuario_escolhe_jogada (n, m):

    #print('É a sua vez!')
    print('Agora restam {} peças no tabuleiro.'.format(n, m))
    usuariom = int(input('Quantas peças você vai retirar? '))

    while usuariom > m or usuariom <= 0:

        #print('É a sua vez!')
        print('Oops! Jogada inválida! Tente de novo')
        usuariom = int(input('Quantas peças você vai retirar? '))

    return usuariom


def partida():

    #n = int(input('Digite o numero de peças do jogo: '))
    n = int(input('Quantas pecas?'))

    #m = int(input('Digite o numero maximo de peças a retirar por rodada: '))
    m = int(input('Limite de peças por jogada?: '))


    rodada = 1

    proximojogador = 0

    while n > 0:

        if rodada == 1:

            if n % (m + 1) == 0:

                print('\nVocê começa!\n')
                n -= usuario_escolhe_jogada(n, m)
                proximojogador = 2

            else:

                print('\nComputador Começa!\n')
                n -= computador_escolhe_jogada(n, m)
                proximojogador = 1

        else:

            if proximojogador == 1:

                n -= usuario_escolhe_jogada(n, m)
                proximojogador = 2

            elif proximojogador == 2:

                n -= computador_escolhe_jogada(n, m)
                proximojogador = 1

        if n == 0:

            if proximojogador == 1:

                print('Fim de jogo! O computador ganhou!!')
                return 2

            elif proximojogador == 2:

                print('Você venceu!!')
                return 1

        rodada += 1


def main():

    menu = 10

    while not menu == 0:

        print('Bem vindo ao jogo NIM! Escolha:\n')
        print('1 - para jogar uma partida isolada')
        print('2 - para jogar um campeonato 2')
        #print('0 - Sair')
        opcao = int(input('\nDigite sua opção:'))

        if opcao == 1:

            partida()

        elif opcao == 2:

            '''quantidadeDePartidas = int(input('Digite a quantidade de partidas:'))'''
            print('\nVoce escolheu um campeonato!')
            quantidadeDePartidas = 3
            partidas = 1

            jogadorUm = 0
            jogadorDois = 0

            while partidas <= quantidadeDePartidas:
                
                print('\n**** Rodada {} ****\n'.format(n))

                vencedor = partida()

                if vencedor == 1:

                    jogadorDois += 1

                else:

                    jogadorUm += 1

                '''print('----Placar da Rodada----')
                print('Computador: {} vitórias'.format(jogadorUm))
                print('Usuário: {} vitórias'.format(jogadorDois))'''

                partidas += 1
                
            print('**** Final do campeonato! ****')
            print('Placar: Você {} x {} Computador'.format(jogadorDois, jogadorUm))
            
            '''
            if jogadorUm > jogadorDois:

                print('-----Computador foi Campeão!!!')

            elif jogadorDois > jogadorUm:

                print('-----Usuário foi Campeão!!!')

            else: print('-----Empate!!!')'''

        else:

            menu = opcao

main()
