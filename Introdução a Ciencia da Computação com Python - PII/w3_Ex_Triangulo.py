'''
Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos 
lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros 
e devolve um valor inteiro correspondente ao perímetro do triângulo.
'''

class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        
    def a(self):
        return self.lado_a
    
    def b(self):
        return self.lado_b
    
    def c(self):
        return self.lado_c
    
    def perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c
    
    def tipo_lado(self, a, b, c):
        if a + b + c == 3 * a:
            return 'equilátero'
        elif self.lado_a != self.lado_b != self.lado_c:
            return 'escaleno'
        else:
            return 'isóceles'