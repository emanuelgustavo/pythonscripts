def primeiro_lex(lista_strings):
    index_lista_strings = 1
    primeira_string = lista_strings[0]
    
    while index_lista_strings < len(lista_strings):
                
        proxima_string = lista_strings[index_lista_strings]
        
        if primeira_string > proxima_string:
            primeira_string = proxima_string
        
        index_lista_strings += 1
    
    return primeira_string

def teste(lista_strings, esperado):
    
    if esperado == primeiro_lex(lista_strings):
        print('OK!')
    else:
        print('Resultado fora do esperado')
        
teste(['oĺá', 'A', 'a', 'casa'], 'A')

teste(['AAAAAA', 'b'], 'AAAAAA')

