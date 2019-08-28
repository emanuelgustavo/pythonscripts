'''
produtos
'''
class Produto:
    def __init__(self, cod_produto, nome_produto, caracteristica_produto, tamanho_produto, ncm_produto, valor_produto):    
        self.cod_produto = cod_produto              
        self.nome_produto = nome_produto
        self.caracteristica_produto = caracteristica_produto
        self.tamanho_produto = tamanho_produto
        self.ncm_produto = ncm_produto
        self.valor_produto = valor_produto #valor com desconto do cliente

    def produtos_atributos(self):
        return [
            self.cod_produto,
            self.nome_produto,
            self.caracteristica_produto,
            self.tamanho_produto,
            self.ncm_produto,
            self.valor_produto
            ]
            
            

