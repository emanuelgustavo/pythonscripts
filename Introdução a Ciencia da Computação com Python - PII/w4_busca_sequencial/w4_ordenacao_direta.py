import random

class Ordenador:
    
    def ordenacao_direta(self, lista):
        
        fim = len(lista)
        
        for i in range(fim -1):
            #Inicialmente, o meno elemento já visto é o i-ésimo
            posicao_do_minimo = i
            
            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j
            
            #Coloca o menor elemento encontrado no inicio da sub-lista
            #Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
        
        return lista

    def bolha (self, lista):
        fim = len(lista)

        print(lista)
        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)

def main():

    ordena = Ordenador()
    lista = [random.randint(0,100) for x in range(10000)]
    ordena.bolha(lista)

main()

        
