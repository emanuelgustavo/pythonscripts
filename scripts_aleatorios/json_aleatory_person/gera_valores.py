'''classe para gerar valores aleatorios de idade, nome, sobrenome, sexo
'''
import random
import re
import io

class GeraValores:
    
    def limpa_string_nome(self, lista_nomes):
        nova_lista_nomes = []
        for nome in lista_nomes:
            novo_nome = re.sub('\n', '', nome)
            nova_lista_nomes.append(novo_nome)
        #print(nova_lista_nomes)
        return nova_lista_nomes
    
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
    
    def gera_numero_telefone(self):
        telefone = ''
        for i in range(9):
            if i == 4:
                telefone += '-'
            else:
                telefone += str(random.randint(0,9))
        return telefone

    def gera_idade(self, estagio_vida='crianca'):
        if estagio_vida == 'adulto':
            return random.randint(20,100)
        elif estagio_vida == 'adolescente':
            return random.randint(13,19)
        else:
            return random.randint(0,12)
        
    def gera_nome_filho(self, quantidade_filhos):
        nome_filhos = []
        if quantidade_filhos > 0:
            for filho in range(quantidade_filhos):
                nome_filhos.append(self.gera_nome())
            return nome_filhos
        else:
            return None

    #carrega os nomes do arquivo txt
    def carrega_arquivo(self, arquivo):
        '''with open(arquivo, 'r') as arq_lista_nomes:
            lista_arquivo = arq_lista_nomes.readlines()
        lista_arquivo = self.limpa_string_nome(lista_arquivo)
        '''
        lista_arquivo = []
        for line in io.open(arquivo, encoding="ISO-8859-1"):
            lista_arquivo.append(line)
        return lista_arquivo
    
def main():
    gv = GeraValores()
    nome_completo = gv.gera_nome() + ' ' + gv.gera_sobrenome()
    telefone = gv.gera_numero_telefone()
    idade = gv.gera_idade('adulto')
    filhos = gv.gera_nome_filho(random.randint(0,10))
    print(nome_completo, telefone, idade, filhos)

if __name__ == "__main__":
    main()
        
