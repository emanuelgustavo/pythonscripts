import re

class LimpaArquivo:
    #carrega os sobrenomes do arquivo sobrenomes_txt
    def carrega_arquivo(self):
        with open('sobrenomes_.txt', 'r') as arq_sobrenomes:
            sob_nomes = arq_sobrenomes.readlines()
        #remove a sujeira da string sobrenome e cria a lista sobrenomes
        sobrenomes = [re.sub(r'– ', '', sobrenome).strip() for sobrenome in sob_nomes]

        return sobrenomes
    #escreve o arquivo com os sobrenomes 'limpos'
    def escreve_arquivo(self, lista_sobrenomes):
        #cria variável string para receber os sobrenomes
        sobrenomes_arquivo = ''    
        for sobrenome in lista_sobrenomes:
            if 'Letra' not in sobrenome:
                #escreve cada sobrenome separado por '\n'
                sobrenomes_arquivo += sobrenome + '\n'

        with open('sobrenomes.txt', 'w') as arq_sobrenome:
            arq_sobrenome.write(sobrenomes_arquivo)

def main():
    lp = LimpaArquivo()
    sobrenomes = lp.carrega_arquivo()
    lp.escreve_arquivo(sobrenomes)

if __name__ == '__main__':
    main()
        
        
