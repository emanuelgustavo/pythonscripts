# -*- Coding: UTF-8 -*-
#coding: utf-8

import random
op = 's'

def main():
    
    op = 's'
    while op == 's':
        game()
        op = input('Continuar a jogar?  (s = sim / n = não) ')

def game():

    n = int(input('Numero de tentativas: '))
    i = 1
    x = random.randint(1, 100)
    acertou = False
    tentativas = 1

    while i <= n:
        chute = int(input('Digite um numero: '))    
        if chute == x:
            print('Você acertou')
            acertou = True
            i = n
        else:
            if chute < x:
                print('O valor é maior!')
            else:
                print('O valor é menor!')
        i += 1
        tentativas += 1

    if not acertou:
        print('O número correto é {}'.format(x))
    else:
        print('Você acertou o número em {}'.format(tentativas))
        
    
main()