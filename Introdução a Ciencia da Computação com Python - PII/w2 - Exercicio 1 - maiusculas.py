def maiusculas(frase):
    '''recebe uma frase string e retorna uma string com as letras maiusculas do texto'''
    maiusculas = ''
    for palavra in frase:
        for char in palavra:
            if ord(char) in range(65, 91):
                maiusculas += char

    return maiusculas

print(maiusculas('Programamos em python 2?'))

print(maiusculas('Programamos em Python 3.'))

print(maiusculas('PrOgRaMaMoS em python!'))
