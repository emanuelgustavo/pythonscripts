import random

def main():    
    #print(verificaResultado(aposta(), sorteio()))
    #simulaSorteios()
    print(sorteiosReal())
    
        

def sorteiosReal():
    with open('megasena.txt', 'r') as arquivo:
        sorteios = arquivo.readlines()
    matriz_sorteios = []
    for line in sorteios:
        linha_matriz = []
        linha_dados = line.split(';')
        for data in linha_dados:
            linha_matriz.append(data)
        matriz_sorteios.append(linha_matriz)
        #sorteio, data,  dezena1, dezena2, dezena3, dezena4, dezena5, dezena6 = line.split(';')
        #print('{} {} {} {} {} {} {} {} \n'.format(sorteio, data,  dezena1, dezena2, dezena3, dezena4, dezena5, dezena6))
    return matriz_sorteios

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
    #print(aposta)
    return aposta

def sorteio():
    sorteados = []
    while len(sorteados) < 6:
        dezena = random.randint(1,60)
        if dezena not in sorteados:
            sorteados.append(dezena)
    #print(sorteados)
    return sorteados

def verificaResultado(aposta, sorteados):
    acertos = 0
    for dezena in aposta:
        if dezena in sorteados:
            acertos += 1
    #print(acertos)
    return acertos

def simulaSorteios():
    acertos = 0
    tentativas = 1
    frequenciaAcerto = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
        }    
    freqSorteado = {}
    while tentativas <= 1000000:
        aposta = apostaVencedora()
        sorteados = sorteio()
        resultado = verificaResultado(aposta, sorteados)
        if resultado == 6:
            print('Aposta Vencedora: {}\nSoteio: {}\nTentativas: {}'.format(aposta, sorteados, tentativas))
        print('Tentativas: {}'.format(tentativas))
        if resultado in frequenciaAcerto:
            frequenciaAcerto[resultado] += 1
        tentativas += 1
        for dezena in sorteados:
            if dezena in freqSorteado:
                freqSorteado[dezena] += 1
            else:
                freqSorteado[dezena] = 1
    #print('Frequencia: {}'.format(sorted(frequenciaAcerto)))
    for a in sorted(frequenciaAcerto): 
        print(' {} acertos saiu {} vez(es)'.format(a, frequenciaAcerto[a]))
    for dezena in sorted(freqSorteado): 
        print(' {} saiu {} vez(es)'.format(dezena, freqSorteado[dezena]))
        
def teste():
    apostaTeste = sorteio()
    sorteado = apostaTeste
    resultado = verificaResultado(apostaTeste, sorteado)
    frequenciaAcerto = {
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0
        }
    if resultado in frequenciaAcerto:
        frequenciaAcerto[resultado] += 1
        
    #print('Aposta teste: {}'.format(apostaTeste))
    #print('Sorteado: {}'.format(sorteado))
    print(frequenciaAcerto)
    
main()
#teste()  
