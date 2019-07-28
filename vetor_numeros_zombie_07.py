opcao = 1
numeros = []

while opcao == 1:
    numero = int(input("Digite um numero ou 0 para sair: "))

    if numero == 0:
        opcao = 0
    else:
        numeros.append(numero)
        print(numeros)
