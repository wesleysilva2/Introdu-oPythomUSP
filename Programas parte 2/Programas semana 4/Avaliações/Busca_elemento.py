def busca(lista, elemento):

    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if lista[i] == elemento:
            return i

    return False        