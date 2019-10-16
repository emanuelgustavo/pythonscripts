import w6_Ex2_enocntra_impares
import pytest

class Test_encontra_impares:

    @pytest.fixture
    def impares(self):
        return w6_Ex2_enocntra_impares.Encontra_impares()

    @pytest.mark.parametrize('entrada, esperado', [
        ([1,4,9,25], [1,9,25]),
        ([1], [1]),
        ([1,5,7,9], [1,5,7,9]),
        ([2,4,6,8], []),
        ([2], []),
    ])    
    
    def test_encontra_impares(self, entrada, esperado, impares):
        assert impares.encontra_impares(entrada) == esperado