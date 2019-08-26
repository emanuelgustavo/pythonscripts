'''
Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos 
lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros 
e devolve um valor inteiro correspondente ao perímetro do triângulo.
'''

class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    '''   
    def a(self):
        return self.lado_a
    
    def b(self):
        return self.lado_b
    
    def c(self):
        return self.lado_c
    '''
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a + self.b + self.c == 3 * self.a:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isóceles'
