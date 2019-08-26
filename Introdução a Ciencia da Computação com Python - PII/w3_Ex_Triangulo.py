'''
Exercício 1: Uma classe para triângulos
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos 
lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros 
e devolve um valor inteiro correspondente ao perímetro do triângulo.
'''
import math

class Triangulo:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a + self.b + self.c == 3 * self.a:
            return 'equilátero'
        elif self.a != self.b and self.a != self.c and self.b != self.c:
            return 'escaleno'
        else:
            return 'isóceles'

    def retangulo(self):
        return True if math.sqrt(( self.a**2 + self.b**2 )) == self.c else False

    def semelhantes(self, triangulo):
        if self.a == triangulo.a and self.b == triangulo.b and self.c == triangulo.c:
            return True
        elif self.a % triangulo.a == 0 and self.b % triangulo.b == 0 and self.c % triangulo.c == 0:
            return True
        elif triangulo.a % self.a == 0 and triangulo.b % self.b == 0 and triangulo.c % self.c == 0:
            return True
        else:
            return False   
        
            
            

    
