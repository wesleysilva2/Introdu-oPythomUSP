import bhaskara_testes
import pytest # importando o modulo de testes para poder usar a fixture
class TestBhaskara:

    @pytest.fixture # usando para não repetir o b em todos os testes
     def b(self): 
         return bhaskara_testes.Bhaskara()
    
    def testa_uma_raiz(self, b):
        assert b.calcula_raiz(1,0,0) == (1,0)
        
    def testa_duas_raizes(self, b):
        assert b.calcula_raiz(1,-5,6) == (2, 3, 2)

    def testa_zero_raizes(self, b):
        assert b.calcula_raiz(10,10,10) == (0)

    def testa_raiz_negativa(self, b):
        assert b.calcula_raiz(10,20,10) == (1, -1)
