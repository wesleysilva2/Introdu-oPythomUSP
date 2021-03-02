# Para busca binaria, para funcionar recursivamente, seria assim, a gente procura arcabouço no dicionario
# ai a gente vai na metade dele e ver faca, arcabouço e menor que faca no alfabeto, então a gente tem que olhar
# do lado esquerdo do dicionario, camamos recursivamente a função de busca binaria e buscamos na metade esquerda, e assim susessivamente
import pytest

def busca_binaria(lista, elemento_buscado, min=0, max = None): # min e max opicionais, se não dizer onde ele vai na lista completa
    if max == None:
        max = len(lista) -1

    if max < min: # se o max for menor que o mim, quer dizer que o valor não foi encontrado
        return False
    else: # calculando o novo meio
        meio = min + (max-min)//2

    if lista[meio] > elemento_buscado:
        return busca_binaria(lista, elemento_buscado, min, meio-1) # chamada recursiva para ir na esquerda da lista passando o novo meio

    elif lista[meio] < elemento_buscado:
        return busca_binaria(lista, elemento_buscado, meio+1, max)# Chamando recursivamente para o lado direito agora

    else: # Quando o elemento esta exatamente no meio
        return meio
        

a = [10,20,30,40,50,60,70,80,90]

@pytest.mark.parametrize("lista, valor, esperado",[
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 70, 6),
    (a, 80, 7),
    (a, 90, 8),
    (a, 100, False),
    (a, 15, False),
    (a, -10, False)
    ])

def teste_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado  
