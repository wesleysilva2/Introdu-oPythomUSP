def fibonacci(n):
    if n < 2: # seria a base da recurção, onde o problema e pequeno
        return n
    else: # aqui ja cai fora da base da recurção

        return fibonacci(n-1) + fibonacci(n-2)    #Chamada recursiva chamando a propria função dentro dela 

import pytest # Rodando testes

@pytest.mark.parametrize("entrada, esperado",[ 
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21)
    ])

def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado  
