def computador_escolhe_jogada(quantidadePecas, pecasRetirar):

    print('É a vez do computador!')
    print('Peças em jogo: {} | Peças permitidas retirar na rodada: {}'.format(quantidadePecas, pecasRetirar))

    if quantidadePecas <= pecasRetirar:

        print('O computador retirou: {}'.format(quantidadePecas))
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

    print('É a sua vez!')
    print('Peças em jogo: {} | Peças permitidas retirar na rodada: {}'.format(quantidadePecas, pecasRetirar))
    usuarioPecasRetirar = int(input('Quantas peças deseja retirar? '))

    while usuarioPecasRetirar > pecasRetirar:

        print('É a sua vez!')
        print('Peças em jogo: {} | Peças permitidas retirar na rodada: {}'.format(quantidadePecas, pecasRetirar))
        usuarioPecasRetirar = int(input('Jogada Inválida! Digite novamente > Quantas peças deseja retirar? '))

    return usuarioPecasRetirar


def partida():

    quantidadePecas = int(input('Digite o numero de peças do jogo: '))

    pecasRetirar = int(input('Digite o numero maximo de peças a retirar por rodada: '))

    rodada = 1

    proximojogador = 0

    while quantidadePecas > 0:

        if rodada == 1:

            if quantidadePecas % (pecasRetirar + 1) == 0:

                print('Usuário pode começar jogando!')
                quantidadePecas -= usuario_escolhe_jogada(quantidadePecas, pecasRetirar)
                proximojogador = 2

            else:

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

                print('O computador venceu!!')
                return 2

            elif proximojogador == 2:

                print('Você venceu!!')
                return 1

        rodada += 1


def main():

    menu = 10

    while not menu == 0:

        print('--------------Menu-------------')
        print('1 - Partida única')
        print('2 - Campeonato')
        print('0 - Sair')
        opcao = int(input('Digite sua opção:'))

        if opcao == 1:

            partida()

        elif opcao == 2:

            quantidadeDePartidas = int(input('Digite a quantidade de partidas:'))
            n = 1

            jogadorUm = 0
            jogadorDois = 0

            while n <= quantidadeDePartidas:

                vencedor = partida()

                if vencedor == 1:

                    jogadorDois += 1

                else:

                    jogadorUm += 1

                print('----Placar da Rodada----')
                print('Computador: {} vitórias'.format(jogadorUm))
                print('Usuário: {} vitórias'.format(jogadorDois))

                n += 1

            if jogadorUm > jogadorDois:

                print('-----Computador foi Campeão!!!')

            elif jogadorDois > jogadorUm:

                print('-----Usuário foi Campeão!!!')

            else: print('-----Empate!!!')

        else:

            menu = opcao

main()
