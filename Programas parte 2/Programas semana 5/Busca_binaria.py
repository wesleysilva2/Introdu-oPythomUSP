class Buscador:
    def busca_sequencial(self, lista,x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro_elemento = 0 # primeiro e ultimo elemento da lista
        ultimo_elemento = len(lista)-1

        while primeiro_elemento <= ultimo_elemento: # se isso rolar quer dizer que não foi encontrado o x
            meio = (primeiro_elemento + ultimo_elemento) // 2 # pegando o elemento do meio da lista
            if lista[meio] == x: # encontrou retorna o x 
                return meio # esse mesmo if vai dar conta de encontrar o x, mesmo que n de true de primeira
            
            else:
                if x < lista[meio]: # se for menor ele esta na primeira metade da lista
                    ultimo_elemento = meio - 1 # dizemos que o ultimo elemento agora e do meio para baixo

                else: # x é maior que o meio ou seja temos que olhar a segunda metade a da direita
                    primeiro_elemento = meio + 1 # dizemos agora que o primeiro elemento e do meio para cima

        return -1 # se chegar aqui o elemento não esta na lista
    
    
