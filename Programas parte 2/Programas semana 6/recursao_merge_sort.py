def merge_sort(lista):
    if len(lista) <= 1: # Base da recursao
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio]) # Chamada recursibvva para dividir por 2 o lado esquerdo
    lado_direito = merge_sort(lista[meio:]) # chamando o lado direito da lista para dividir recursivamente

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito): # funcão que serve para intercalar os lados e devolver ordenado
    if not lado_esquerdo: # base da recurção 
        return lado_direito
    if not lado_direito: # base 
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]: # Recurção mesmo
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])