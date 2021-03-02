def fatorial(n):
    if n < 1: # seria a base da recurção, onde o problema e pequeno
        return 1
    else: # aqui ja cai fora da base da recurção

        return n * fatorial(n-1)    #Chamada recursiva chamando a propria função dentro dela 

import pytest # Rodando testes

@pytest.mark.parametrize("entrada, esperado",[ 
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado  
        
