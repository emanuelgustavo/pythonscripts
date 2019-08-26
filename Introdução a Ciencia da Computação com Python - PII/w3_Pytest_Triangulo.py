import pytest
import w3_Ex_Triangulo as Triangulo

class Test_Triangulo:
    
    '''@pytest.fixture
    def triangulo(self):
        return Triangulo.Triangulo()
    '''
    @pytest.mark.parametrize('a, b, c, esperado', [
        (4, 4, 4, 'equilátero'),
        (3, 4, 5, 'escaleno'),
    ])
    
    def test_triangulo(self, a, b, c, esperado):
        triangulo = Triangulo.Triangulo(a, b, c)
        assert triangulo.tipo_lado(a, b, c) == esperado
    