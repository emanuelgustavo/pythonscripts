import pytest
import w3_Cubo

class Test_Cubo:
    
    @pytest.fixture
    def cubo(self):
        return w3_Cubo.Cubo()
    
    @pytest.mark.parametrize('entrada, esperado', [
        (0,0),
        (1,1),
        (2,8),
        (-1,-1),
        (-2, -8),
        (10, 1000),
        (-3, -27)
    ])
    
    def test_cubo(self, cubo, entrada, esperado):
        assert cubo.calcula_cubo(entrada) == esperado
        