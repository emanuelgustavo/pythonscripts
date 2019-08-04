def inverte_sequencia():
    numeros = []
    numero = 1
    while numero != 0:        
        numero = int(input('Digite um numero: '))
        numeros.append(numero)
    elemento = len(numeros)
    while elemento >= 0:
        if numeros[elemento-1] == 0:
            print('')
        else:
            print(numeros[elemento-1])
        elemento -= 1
            
inverte_sequencia()