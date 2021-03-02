import pytest 

def fatorial (n):
    i = fat = 1
    while i < n:
        fat = fat * i
        i = i + 1
    return fat


@pytest.mark.parametrize("entrada, esperado",[
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
