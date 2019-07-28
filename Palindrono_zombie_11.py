'''
palindrono
'''
sair = 0

while sair == 0:
    
    palavra = str(input("Digite uma palavra ou 0 para sair: "))

    if palavra == "0":
        sair = 1
    elif palavra == palavra[::-1]:
        print("%s é um palindrono!" %palavra)
    else:
        print("%s não é um palindrono!" %palavra)
