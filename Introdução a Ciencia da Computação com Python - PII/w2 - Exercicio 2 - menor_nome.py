def menor_nome(nomes):
    ''' recebe uma lista de strings com nome de pessoas como parâmetro e
    devolve o nome mais curto presente na lista'''
    menor = nomes[0]
    for i in range(len(nomes)):
        if len(nomes[i].strip()) < len(menor.strip()):
            menor = nomes[i].strip()
    menor.replace(' ', '')
    return menor.capitalize()

print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
# deve devolver 'José'

print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
# deve devolver 'José'

print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))
# deve devolver José

print(menor_nome(['LU   ', ' josé ', 'PAULO', 'Catarina']))
