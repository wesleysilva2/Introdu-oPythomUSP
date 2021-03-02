def cria_matriz(num_linhas, num_colunas, valor):
    "(int,int,valor) -> matriz (lista de listas)"
    "Cria e retorna uma matriz com nun_linhas linhas e num_colunas"
    "colunas em que cada elemento é igual ao valor dado"
    matriz = [] # lista vazia, guarda as linhas da matriz
    for i in range(num_linhas): # numero de vezes que ele vai executar 
        # cria a lista i
        linha = [] # lista vazia, guarda as colunas
        for j in range(num_colunas): # executa dependedo do numero de colunas
            linha.append(valor) # adiciona o valor escolhido pelo usuario na coluna 

        # adiciona linha á matriz
        matriz.append(linha) # acabou a coluna vai para proxima linha e reinicia
    return matriz      