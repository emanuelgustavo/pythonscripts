def conta_letras(frase, contar='vogais'):
    'recebe uma frase e o tipo da letra a ser contado e retorna a quantidade'
    
    total_vogais = 0
    total_consoantes = 0
    
    for char in frase:
        if contar == 'vogais':
            if char in 'aeiou':
                total_vogais += 1
        elif contar == 'consoantes':
            if char not in 'aeiou' and char != ' ':
                total_consoantes += 1
    
    if contar == 'vogais':
        return total_vogais
    else:
        return total_consoantes

'''
def teste(string_teste, esperado, contar='vogais'):
    
    string = string_teste
    resultado = esperado
    
    
    if esperado == conta_letras(string_teste, contar):
        print('Resultado Ok')
    else:
        print('Resultado fora do esperado')

teste('programamos em python', 6)

teste('programamos em python', 6, 'vogais')

teste('programamos em python', 13, 'consoantes')
'''