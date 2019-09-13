'''classe para gerar valores aleatorios de idade, nome, sobrenome, sexo
'''
import random

class GeraValores:
    def carrega_arquivo(self, arquivo):
        with open(arquivo, 'r') as arq_lista_nomes:
            lista_arquivo = arq_lista_nomes.readlines()
        return lista_arquivo
    #carrega os nomes do arquivo txt
    def carrega_nome(self):
        lista_nomes = self.carrega_arquivo('nomes.txt')
        return lista_nomes
    
    def carrega_sobrenome(self):
        lista_nomes = self.carrega_arquivo('sobrenomes.txt')
        return lista_nomes
    
    def gera_nome(self):
        nomes = self.carrega_nome()
        nome = nomes[random.randint(0, len(nomes)-1)]
        return nome

    def gera_sobrenome(self):
        sobrenomes = self.carrega_sobrenome()
        nome = sobrenomes[random.randint(0, len(sobrenomes)-1)]
        return nome

def main():
    gv = GeraValores()
    print(gv.gera_nome(), gv.gera_sobrenome())

if __name__ == "__main__":
    main()
        
