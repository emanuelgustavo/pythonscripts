def computador_escolhe_jogada(quantidadePecas, pecasRetirar):

    #print('É a vez do computador!')
    #print('Peças em jogo: {} | Peças permitidas retirar na rodada: {}'.format(quantidadePecas, pecasRetirar))

    if quantidadePecas <= pecasRetirar:

        print('O computador retirou: {}'.format(quantidadePecas if quantidadePecas > 1 else 'uma'))
        return quantidadePecas

    elif quantidadePecas > pecasRetirar:

        n = 1

        while n < pecasRetirar:

            testeQuantidadePecas = quantidadePecas - n

            if testeQuantidadePecas % (pecasRetirar + 1) == 0:

                break

            n += 1

        print('O computador retirou: {}'.format(n))
        return n


def usuario_escolhe_jogada (quantidadePecas, pecasRetirar):

    #print('É a sua vez!')
    print('Agora restam {} peças no tabuleiro.'.format(quantidadePecas, pecasRetirar))
    usuarioPecasRetirar = int(input('Quantas peças você vai retirar? '))

    while usuarioPecasRetirar > pecasRetirar:

        #print('É a sua vez!')
        print('Oops! Jogada inválida! Tente de novo')
        usuarioPecasRetirar = int(input('Quantas peças você vai retirar? '))

    return usuarioPecasRetirar


def partida():

    #quantidadePecas = int(input('Digite o numero de peças do jogo: '))
    quantidadePecas = int(input('Quantas pecas?'))

    #pecasRetirar = int(input('Digite o numero maximo de peças a retirar por rodada: '))
    pecasRetirar = int(input('Limite de peças por jogada?: '))


    rodada = 1

    proximojogador = 0

    while quantidadePecas > 0:

        if rodada == 1:

            if quantidadePecas % (pecasRetirar + 1) == 0:

                print('Usuário pode começar jogando!')
                quantidadePecas -= usuario_escolhe_jogada(quantidadePecas, pecasRetirar)
                proximojogador = 2

            else:

                print('Computador Começa:')
                quantidadePecas -= computador_escolhe_jogada(quantidadePecas, pecasRetirar)
                proximojogador = 1

        else:

            if proximojogador == 1:

                quantidadePecas -= usuario_escolhe_jogada(quantidadePecas, pecasRetirar)
                proximojogador = 2

            elif proximojogador == 2:

                quantidadePecas -= computador_escolhe_jogada(quantidadePecas, pecasRetirar)
                proximojogador = 1

        if quantidadePecas == 0:

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
            quantidadeDePartidas = 3
            n = 1

            jogadorUm = 0
            jogadorDois = 0

            while n <= quantidadeDePartidas:
                
                print('\n**** Rodada {} ****\n'.format(n))

                vencedor = partida()

                if vencedor == 1:

                    jogadorDois += 1

                else:

                    jogadorUm += 1

                '''print('----Placar da Rodada----')
                print('Computador: {} vitórias'.format(jogadorUm))
                print('Usuário: {} vitórias'.format(jogadorDois))'''

                n += 1
                
            print('**** Final do campeonato! ****')
            print('Placar: Você {} x {} Computador')
            
            '''
            if jogadorUm > jogadorDois:

                print('-----Computador foi Campeão!!!')

            elif jogadorDois > jogadorUm:

                print('-----Usuário foi Campeão!!!')

            else: print('-----Empate!!!')'''

        else:

            menu = opcao

main()
