import bhaskara_testes
import pytest # importando o modulo de testes para poder usar a fixture e parametrize
class TestBhaskara:
    # usando para não repetir o b em todos os teste

    @pytest.mark.parametrize("valor1, valor2, valor3, esperado1,esperado2,esperado3",[
        (1,0,0, 1,0),
        (1,-5,6, 2,3,2),
        (10,10,10 , 0),
        (10,20,10, 1,-1)
        ])
     
    def testa_uma_raiz(valor1,valor2,valor3, esperado1,esperado2,esperado3):
        assert b.calcula_raiz(valor1,valor2,valor3) == (esperado1,esperado2,esperado3)
        
        
