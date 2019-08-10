#!-*- conding: utf8 -*-
import re
import operator

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma 
  assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de 
    similaridade nas assinaturas.'''
    somatorio_ass = 0
    index = 0
    if len(as_a) == len(as_b):
        while index < len(as_b):
            somatorio_ass += as_a[index] - as_b[index]
            index += 1
    indice_de_similaridade = abs(somatorio_ass) / 6
    return indice_de_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    '''total_palavras_texto = n_total_palavras_texto(lista_palavras(texto))
    total_palavras_diferentes = n_palavras_diferentes(lista_palavras(texto))
    total_palavras_unicas = n_palavras_unicas(lista_palavras(texto))
    
    relacao_type_token = total_palavras_diferentes / total_palavras_texto    
    razao_hapax = total_palavras_unicas / total_palavras_texto

    print(lista_palavras(texto))
    print(soma_tamanho_palavras(lista_palavras(texto)))
    print(total_palavras_texto)
    tamanho_medio_palavras = soma_tamanho_palavras(lista_palavras(texto)) / total_palavras_texto

    lista_sentencas = separa_sentencas(texto)
    tamanho_total_sentencas = soma_tamanho_sentencas(lista_sentencas)    
    tamanho_medio_sentencas = tamanho_total_sentencas / len(lista_sentencas)

    total_frases_texto = 0
    lista_frases_texto = []
    for sentenca in lista_sentencas:
      total_frases = len(separa_frases(sentenca))
      lista_frases_texto.append(separa_frases(sentenca))
      total_frases_texto += total_frases
    #print('total_frases_texto: {}'.format(total_frases_texto))
    complexidade_sentenca = total_frases_texto / len(lista_sentencas)
    tamanho_medio_frase = soma_tamanho_frase(lista_frases_texto) / total_frases_texto
    
    return [tamanho_medio_palavras, relacao_type_token, razao_hapax, tamanho_medio_sentencas, complexidade_sentenca, tamanho_medio_frase]
    '''
    lista_sentencas_texto = separa_sentencas(texto)
    lista_palavras_texto = []
    lista_frases_texto = []
    
    total_palavras_texto = 0
    total_frases_texto = 0
    total_tamanho_sentencas = 0
    total_sentencas_texto = 0
    
    for sentenca in lista_sentencas_texto:
        lista_frases_texto.append(separa_frases(sentenca))
        total_tamanho_sentencas += len(sentenca)
        total_sentencas_texto += 1
        
    for frase_i in lista_frases_texto:
        for frase_j in frase_i:
            lista_palavras_frase = []            
            lista_palavras_frase.append(separa_palavras(frase_j))
            for frase in lista_palavras_frase:
                total_frases_texto += 1
                for palavra in frase:
                    lista_palavras_texto.append(palavra)
    
    total_palavras_texto = len(lista_palavras_texto)
    total_palavras_diferentes = n_palavras_diferentes(lista_palavras_texto)
    total_palavras_unicas = n_palavras_unicas(lista_palavras_texto)
    
    relacao_type_token = total_palavras_diferentes / total_palavras_texto    
    razao_hapax = total_palavras_unicas / total_palavras_texto
    complexidade_sentenca = total_frases_texto / len(lista_sentencas_texto)
    tamanho_medio_frase = soma_tamanho_frase(lista_frases_texto) / total_frases_texto
    tamanho_medio_palavras = soma_tamanho_palavras(lista_palavras_texto) / total_palavras_texto
    tamanho_medio_sentencas = total_tamanho_sentencas / total_sentencas_texto

    return [tamanho_medio_palavras, relacao_type_token, razao_hapax, tamanho_medio_sentencas, complexidade_sentenca, tamanho_medio_frase]
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do 
    texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    as_bs = []
    indice_lista = 0
    
    for texto in textos:
        as_bs.append(calcula_assinatura(texto))
        
    indices_similaridade = []
    
    for ass in as_bs:
        indices_similaridade.append(compara_assinatura(ass_cp, ass))
        
    texto_infectado = 0
    while indice_lista < len(indices_similaridade)-1:
        if indices_similaridade[indice_lista + 1] < indices_similaridade[texto_infectado]:
            texto_infectado = indice_lista+1
        indice_lista += 1
    return texto_infectado+1

def n_total_palavras_texto(listaPalavras):
    '''Recebe uma lista com palavras e retorna o total de palavras'''
    return len(listaPalavras)
    
def lista_palavras(texto):
    '''Recebe um texto e retorna uma lista com as palavras do texto'''
    listaPalavras = re.split(r'[ ,.:"\[\]\;\(\)]+',texto)
    sujeiras = '.,'
    for palavra in listaPalavras:
      index = listaPalavras.index(palavra)
      novaPalavra = palavra
      for char in sujeiras:
        novaPalavra = novaPalavra.replace(char, '')
      listaPalavras[index] = novaPalavra
          
    return listaPalavras

def soma_tamanho_palavras(lista_palavras):
    total_tamanho_palavras = 0
    for palavra in lista_palavras:
        total_tamanho_palavras += len(palavra)
    #print('Total tamanho palavras: {}'.format(total_tamanho_palavras))
    return total_tamanho_palavras

def soma_tamanho_sentencas(lista_sentencas):
    '''Recebe uma lista de sentencas e retorna o tamanho total das sentenças'''
    total_sentencas = 0
    for sentenca in lista_sentencas:
        total_sentencas += len(sentenca)
    #print('Total tamanho sentencas texto: {}'.format(total_sentencas))
    return total_sentencas

def total_frases_texto(lista_sentencas):
   '''recebe uma lista de frases e retorna o total de frases nas sentencas'''
   total_frases = 0
   for frase in lista_sentencas:
       total_frases += 1
       #print('Frase {} : {}'.format(lista_sentencas.index(frase), frase))
   #print('Total frases texto: {}'.format(total_frases))
   return total_frases

def soma_tamanho_frase(lista_frases):
    tamanho_frases = 0
    sujeiras = '.,'
    for frase in lista_frases:
      for palavra in frase:
        for char in palavra:
          if char not in sujeiras:
            tamanho_frases += 1      
    #print(tamanho_frases)
    return tamanho_frases

def teste():
    texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    esperado = [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]
    retorno = (calcula_assinatura(texto))
    if esperado == retorno:
      print('Chave OK!')
    else:
      print('Erro!')
    print('Retorno: {}'.format(retorno))
    print('Esperado: {}'.format(esperado))

def main():
    '''Gerencia o detector de coh-piah'''
    as_a = le_assinatura()
    textos = le_textos()
    print('O autor do texto {} está infectado com COH-PIAH'.format(avalia_textos(textos, as_a)))

    '''linhas para teste'''
    #as_a = ass_teste()
    #textos = lista_textos_ex()
    #print('O autor do texto {} está infectado com COH-PIAH'.format(avalia_textos(textos, as_a)))
    #teste()
    #testa_assinatura()
    #texto = 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
    #texto = 'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
    #texto = 'Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia.'
    #print(calcula_assinatura(texto))
        

def lista_textos_ex():
    textos = [
        'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.',
        'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
        'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
        ]
    return textos

def testa_assinatura():
    ass_a = [4.34, 0.05, 0.02, 12.81, 2.16, 0.0]
    ass_b = [3.96, 0.05, 0.02, 22.22, 3.41, 0.0]
    print(compara_assinatura(ass_a, ass_b))

def ass_teste():
    wal = 4.79
    ttr = 0.72
    hlr = 0.56
    sal = 80.5
    sac = 2.5
    pal = 31.6
    return [wal, ttr, hlr, sal, sac, pal]
    
main()
