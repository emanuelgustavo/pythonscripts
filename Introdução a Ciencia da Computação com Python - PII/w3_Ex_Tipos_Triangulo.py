'''Exercício 2: Tipos de triângulos
Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que 
devolve uma string dizendo se o triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não deve devolver isóceles.'''

class Tipos_Triangulo:
    
    def tipo_lado(self):
        if self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
            return 'isóceles'
        elif self.lado_a != self.lado_b != self.lado_c:
            return 'escaleno'
        else:
            return 'equilátero'