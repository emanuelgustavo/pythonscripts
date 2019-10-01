import random as rd

numero = rd.randint(0,100)
tentativas = 1
acerto = False

while not acerto:
    print('Tentativa {}'.format(tentativas))
    aposta = int(input('Digite um numero: '))
    tentativas += 1
    if aposta == numero:
        acerto = True
        print('Você acerto o número')
    if tentativas > 3:
        acerto = True
    
if tentativas > 3:
    print('Você usou todas as tentativas e não acertou o número {}'.format(numero))
    
