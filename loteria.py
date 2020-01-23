import random

def sorteio():
    pass

def aposta():
    aposta = []
    while len(aposta) < 6:
        numero = int(input('Digite um numero de 1 a 60'))
        while numero < 1 or numero > 60:
             numero = int(input('Digite novamente!'))
        else:
            aposta.append(numero)
    return aposta

def main():
    print(aposta())
    
main()