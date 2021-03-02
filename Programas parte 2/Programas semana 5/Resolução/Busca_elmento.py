def busca(lista, elemento):
    primeiro_elemento = 0 # primeiro e ultimo elemento da lista
    ultimo_elemento = len(lista)-1
    

    while primeiro_elemento <= ultimo_elemento: # se isso rolar quer dizer que não foi encontrado o x
        meio = (primeiro_elemento + ultimo_elemento) // 2 # pegando o elemento do meio da lista
        if lista[meio] == elemento: # encontrou retorna o x
            print(meio)
            return meio# esse mesmo if vai dar conta de encontrar o x, mesmo que n de true de primeira
            
        else:
            if elemento < lista[meio]: # se for menor ele esta na primeira metade da lista
                if ultimo_elemento == 0:
                    ultimo_elemento = meio - 1 # dizemos que o ultimo elemento agora e do meio para baixo
                    print(meio)
                else:
                    print(meio)
                    ultimo_elemento = meio - 1
                    
            else: # x é maior que o meio ou seja temos que olhar a segunda metade a da direita
                if primeiro_elemento == 0:
                    primeiro_elemento = meio + 1
                    print(meio)
                else:
                    print(meio)
                    primeiro_elemento = meio + 1 # dizemos agora que o primeiro elemento e do meio para cima
                

    return False # se chegar aqui o elemento não esta na lista
