'''
Script para completar tabela de um cliente em txt
86047388000100|70140 NZF-20                  	|POLTRONA SONORA NZF FAIXA C DE TECIDO SEM COMPOSE (104 X 83 X 90)				|UN |94016000|NAO|00000|00000|00000|000001995430|000000000000|000000000|000000000|
86047388000100|70140 NZF-20                  	|POLTRONA SONORA NZF FAIXA C DE TECIDO SEM COMPOSE (104 X 83 X 90)				|UN |94016000|NAO|00000|00000|00000|000001995430|000000000000|000000000|000000000|
'''
import Produto as prod

cnpj = '86047388000100'
acabamentos = ['ACF', 'NEF', 'CTF', 'CHF', 'NZF', 'NGF', 'PEF']
acabamento_nogueira = 'NAF'
faixa_tecidos = ['FAIXA S', 'FAIXA A', 'FAIXA C', 'FAIXA PR']

opcao = 's' #controla o loop, adicionar novos produtos

arq_tabela = open('tabela_SD_james_2019.txt', 'w')
arq_lista_produtos = open('lista_produtos.txt', 'w')
tabela_produtos_novos = ''

lista_produtos = []

while opcao.lower() != 'n':

    tem_estofaria = False
    lamina_nogueira = False

    tem_estofaria = False if input('Produto tem estofaria? s/n: ').lower() == 'n' else True
    lamina_nogueira = False if input('Produto em lamina de nogueira? s/n: ').lower() == 'n' else True

    cod_produto = input('Digite o codigo do produto: ').upper()
    nome_produto = input('Digite o nome do produto: ').upper()
    caracteristica_produto = input('Digite o caracteristica do produto: ').upper()
    tamanho_produto = input('Digite o tamanho do produto comp X alt X larg: ').upper()
    ncm_produto = input('Digite o ncm do produto: ').upper()
    valor_produto = input('Digite o valor do produto: ').upper()

    produto = prod.Produto(cod_produto, nome_produto, caracteristica_produto, tamanho_produto, ncm_produto, valor_produto)
    lista_produtos.append(produto)

    opcao = input('Cadastrar mais produtos? s/n: ')

for produto in lista_produtos:
    linha = ';'
    linha = linha.join(produto.produtos_atributos())    
    print(linha)
    print(produto.produtos_atributos())
    arq_lista_produtos.write(linha)

arq_lista_produtos.close()

for produto in lista_produtos:

    contador_combinacao_produto = 1

    if lamina_nogueira:
        if tem_estofaria:
            for faixa in faixa_tecidos:
                acab = acabamento_nogueira
                string_estofaria = ' DE TECIDO SEM COMPOSE '
                string_linha = ''
                string_pt1 = ''
                string_pt2 = ''
                string_pt3 = ''
                string_pt1 += (cnpj + '|' + produto.cod_produto + ' ' + acab + '-' + str(contador_combinacao_produto) + ('\t'*3))
                string_pt2 += ('|' + produto.nome_produto + ' ' + acab + ' ' + (faixa + string_estofaria if tem_estofaria else produto.caracteristica_produto) + \
                            '(' + produto.tamanho_produto + ')')
                string_pt3 += ('|UN |' + produto.ncm_produto + '|NAO|00000|00000|00000|00000' + produto.valor_produto + '|000000000000|000000000|000000000|')
                string_linha += string_pt1 + string_pt2 + ( ('\t'*4) if len(string_pt2) >= 64 else ('\t'*5) ) + string_pt3 + '\n'

                tabela_produtos_novos += string_linha
                contador_combinacao_produto += 1
        else:
            acab = acabamento_nogueira
            string_estofaria = ' DE TECIDO SEM COMPOSE '
            string_linha = ''
            string_pt1 = ''
            string_pt2 = ''
            string_pt3 = ''
            string_pt1 += (cnpj + '|' + produto.cod_produto + ' ' + acab + '-' + str(contador_combinacao_produto) + ('\t'*3))
            string_pt2 += ('|' + produto.nome_produto + ' ' + acab + ' ' + (faixa + string_estofaria if tem_estofaria else produto.caracteristica_produto) + \
                        '(' + produto.tamanho_produto + ')')
            string_pt3 += ('|UN |' + produto.ncm_produto + '|NAO|00000|00000|00000|00000' + produto.valor_produto + \
                        '|000000000000|000000000|000000000|')
            string_linha += string_pt1 + string_pt2 + ( ('\t'*4) if len(string_pt2) >= 64 else ('\t'*5) ) + string_pt3 + '\n'

            tabela_produtos_novos += string_linha
            contador_combinacao_produto += 1

    else:
        if tem_estofaria:
            for faixa in faixa_tecidos:
                for acab in acabamentos:
                    string_linha = ''
                    string_pt1 = ''
                    string_pt2 = ''
                    string_pt3 = ''
                    string_pt1 += (cnpj + '|' + produto.cod_produto + ' ' + acab + '-' + str(contador_combinacao_produto) + ('\t'*3))
                    string_pt2 += ('|' + produto.nome_produto + ' ' + acab + ' ' + (produto.caracteristica_produto) + \
                                     '(' + produto.tamanho_produto + ')')
                    string_pt3 += ('|UN |' + produto.ncm_produto + '|NAO|00000|00000|00000|00000' + produto.valor_produto + \
                                      '|000000000000|000000000|000000000|')
                    string_linha += string_pt1 + string_pt2 + ( ('\t'*4) if len(string_pt2) >= 64 else ('\t'*5) ) + string_pt3 + '\n'

                    tabela_produtos_novos += string_linha
                    contador_combinacao_produto += 1
        else:
            acab = acabamento_nogueira
            string_estofaria = ' DE TECIDO SEM COMPOSE '
            string_linha = ''
            string_pt1 = ''
            string_pt2 = ''
            string_pt3 = ''
            string_pt1 += (cnpj + '|' + produto.cod_produto + ' ' + acab + '-' + str(contador_combinacao_produto) + ('\t'*3))
            string_pt2 += ('|' + produto.nome_produto + ' ' + acab + ' ' + (faixa + string_estofaria if tem_estofaria else produto.caracteristica_produto) + \
                        '(' + produto.tamanho_produto + ')')
            string_pt3 += ('|UN |' + produto.ncm_produto + '|NAO|00000|00000|00000|00000' + produto.valor_produto + \
                        '|000000000000|000000000|000000000|')
            string_linha += string_pt1 + string_pt2 + ( ('\t'*4) if len(string_pt2) >= 64 else ('\t'*5) ) + string_pt3 + '\n'

            tabela_produtos_novos += string_linha
            contador_combinacao_produto += 1

    if not tem_estofaria:
        for acab in acabamentos:
            string_linha = ''
            string_pt1 = ''
            string_pt2 = ''
            string_pt3 = ''
            string_pt1 += (cnpj + '|' + produto.cod_produto + ' ' + acab + '-' + str(contador_combinacao_produto) + ('\t'*3))
            string_pt2 += ('|' + produto.nome_produto + ' ' + acab + ' ' + (produto.caracteristica_produto) + \
                             '(' + produto.tamanho_produto + ')')
            string_pt3 += ('|UN |' + produto.ncm_produto + '|NAO|00000|00000|00000|00000' + produto.valor_produto + \
                              '|000000000000|000000000|000000000|')
            string_linha += string_pt1 + string_pt2 + ( ('\t'*4) if len(string_pt2) >= 64 else ('\t'*5) ) + string_pt3 + '\n'

            tabela_produtos_novos += string_linha
            contador_combinacao_produto += 1


    #opcao = input('Cadastrar mais produtos? s/n: ')

arq_tabela.write(tabela_produtos_novos)
arq_tabela.close()
