'''classe para gerar valores aleatorios de idade, nome, sobrenome, sexo
'''
import random

class GeraValores:
    def carrega_nome(self):

        lista_nomes = []
        
        with open('nomes.txt', 'r') as arq_lista_nomes:
            lista_nomes = arq_lista_nomes.readlines()

        return lista_nomes

    def gera_nome(self):

        nomes = self.carrega_nome()
        nome = nomes[random.randint(0, len(nomes)-1)]
        return nome

def main():
    gv = GeraValores()
    print(gv.gera_nome())

if __name__ == "__main__":
    main()
        
