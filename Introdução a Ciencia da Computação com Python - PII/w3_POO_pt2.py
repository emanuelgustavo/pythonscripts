'''
introdução a POO em Python
'''
def main():
    carro1 = Carro('Brasilia', 1968, 'Amarela', 80)
    carro2 = Carro('Fusca', 1981, 'Preto', 95)
    
    carro1.acelece(40)
    carro2.acelece(50)
    carro1.acelece(80)
    carro1.pare()
    carro2.acelece(100)

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima
        
    def imprima(self):
        if self.velocidade == 0:
            print('{} {} {}'.format(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_maxima:
            print('{} {} indo a {} km/h'.format(self.modelo, self.cor, self.velocidade))
        else:
            print('{} {} indo muito rápido!'.format(self.modelo, self.ano))
    
    def acelece(self, v):
        self.velocidade = v
        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima
        self.imprima()
    
    def pare(self):
        self.velocidade = 0
        self.imprima()
        
main()
