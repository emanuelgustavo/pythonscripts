#!-*- conding: utf8 -*-
import re

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
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    total_palavras_texto = n_total_palavras_texto(lista_palavras(texto))
    total_palavras_diferentes = n_palavras_diferentes(lista_palavras(texto))
    total_palavras_unicas = n_palavras_unicas(lista_palavras(texto))
    
    relacao_type_token = total_palavras_diferentes / total_palavras_texto    
    razao_hapax = total_palavras_unicas / total_palavras_texto
    
    tamanho_medio_palavras = soma_tamanho_palavras(lista_palavras(texto)) / total_palavras_texto

    lista_sentencas = separa_sentencas(texto)
    tamanho_total_sentencas = soma_tamanho_sentencas(lista_sentencas)
    
    tamanho_medio_sentencas = tamanho_total_sentencas / len(lista_sentencas)
    
    complexidade_sentenca = total_frases_texto(separa_sentencas(texto)) / len(separa_sentencas(texto))
    tamanho_medio_frase = soma_tamanho_frase(separa_sentencas(texto)) / len(separa_sentencas(texto))
    return tamanho_medio_palavras
    
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do 
    texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass

def n_total_palavras_texto(listaPalavras):
    '''Recebe uma lista com palabras e retorna o total de palavras'''
    return len(listaPalavras)
    
def lista_palavras(texto):
    '''Recebe um texto e retorna uma lista com as palavras do texto'''
    listaPalavras = texto.split()
    return listaPalavras

def soma_tamanho_palavras(lista_palavras):
    total_tamanho_palavras = 0
    for palavra in lista_palavras:
        total_tamanho_palavras += len(palavra)
    print('Total tamanho palavras: {}'.format(total_tamanho_palavras))
    return total_tamanho_palavras

def soma_tamanho_sentencas(lista_sentencas):
    '''Recebe uma lista de sentencas e retorna o tamanho total das sentenças'''
    total_sentencas = 0
    for sentenca in lista_sentencas:
        total_sentencas += len(sentenca)
    print('Total sentencas texto: {}'.format(total_sentencas))
    return total_sentencas

def total_frases_texto(lista_sentencas):
    total_frases = 0
    for frase in lista_sentencas:
        total_frases += 1
    print('Total frases texto: {}'.format(total_frases))
    return total_frases

def soma_tamanho_frase(lista_frases):
    tamanho_frases = 0
    for frase in lista_frases:
      tamanho_frases += len(frase)
    print(tamanho_frases)
    return tamanho_frases

def teste():
    #texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    texto = "Esse texto é para testar, a assinatura do identificador de cohpiah."
    #print(lista_palavras(texto))
    #print('Total de palavras no texto: {}'.format(total_palavras_texto(lista_palavras(texto))))
    print(calcula_assinatura(texto))
    print(lista_palavras(texto))
    #print(separa_sentencas(texto))

def main():
    '''Gerencia o detector de coh-piah'''
    '''
    textos = le_textos()
    print(textos)
    for texto in textos:
        print(lista_palavras(texto))
        print(len(lista_palavras(texto)))
        print(calcula_assinatura(texto))
    '''
    teste()
    
main()
