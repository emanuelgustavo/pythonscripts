import random

def main():    
    #print(verificaResultado(aposta(), sorteio()))
    acertos = 0
    tentativas = 1
    while acertos != 6:
        aposta = apostaVencedora()
        sorteados = sorteio()
        acertos = verificaResultado(aposta, sorteados)
        tentativas += 1
        if acertos == 6:
            print('Aposta Vencedora: {}\nSoteio: {}\nTentativas: {}'.format(aposta, sorteados, tentativas))
        print('Tentativas: {}'.format(tentativas))
        
def aposta():
    aposta = []
    while len(aposta) < 6:
        numero = int(input('\nDigite uma dezena: '))
        while numero < 1 or numero > 60 or numero in aposta:
            if numero in aposta:
                print('\nDezena inválida! Dezena já selecionada!')
            else:
                print('\nDezena inválida! Digite uma dezena ente 01 e 60')
            numero = int(input('\nDigite uma dezena: '))
        if numero >= 1 and numero <= 60 and numero not in aposta:
            aposta.append(numero)
        print('Sua aposta: {}'.format(aposta))
    return aposta

def apostaVencedora():
    aposta = []
    while len(aposta) < 6:
        dezena = random.randint(1,60)
        if dezena not in aposta:
            aposta.append(dezena)
    print(aposta)
    return aposta

def sorteio():
    sorteados = []
    while len(sorteados) < 6:
        dezena = random.randint(1,60)
        if dezena not in sorteados:
            sorteados.append(dezena)
    print(sorteados)
    return sorteados

def verificaResultado(aposta, sorteados):
    acertos = 0
    for dezena in aposta:
        if dezena in sorteados:
            acertos += 1
    print(acertos)
    return acertos

main()
    
