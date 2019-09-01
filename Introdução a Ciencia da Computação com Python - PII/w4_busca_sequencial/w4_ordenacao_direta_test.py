import pytest
import w4_ordenacao_direta as Ordena

class Test_ordenacao_direta:
    
    @pytest.mark.parametrize('lista, esperado', [
        ([7,6,2,1,9,3], [1,2,3,6,7,9])
    ])
    
    def test_ordenacao_direta(self, lista, esperado):
        ordenacao = Ordena.Ordenador()
        assert ordenacao.ordenacao_direta(lista) == esperado