import w3_Bhaskara
import pytest

class TestBhaskara:
    
    @pytest.fixture
    def bhaskara(self):
        return w3_Bhaskara.Bhaskara()
    
    @pytest.mark.parametrize('a, b, c, esperado', [
        (1, 0, 0, (1, 0)),
        (10, 10, 10, (0)),
        (1, -5, 6, (2, 3, 2)),
        (10, 20, 10, (1, -1))        
    ])
    
    def test_bhaskara(self, bhaskara, a, b, c, esperado):
        assert bhaskara.calcula_raizes(a, b, c) == esperado
    
    '''
    def testa_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
    
    def testa_duas_raizes(self, b):
        assert b.calcula_raizes(1,-5,6) == (2, 3, 2)
        
    def testa_zero_raizes(self, b):
        assert b.calcula_raizes(10,10,10) == (0)
    
    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10,20,10) == (1, -1)
    '''