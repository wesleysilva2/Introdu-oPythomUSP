def cria_matriz(num_linhas, num_colunas):
    "(int,int) -> matriz (lista de listas)"
    "Cria e retorna uma matriz com nun_linhas linhas e num_colunas"
    "colunas em que cada elemento é digitado pelo usuario"
    
    matriz = [] # lista vazia, guarda as linhas da matriz
    for i in range(num_linhas): # numero de vezes que ele vai executar 
        # cria a lista i
        linha = [] # lista vazia, guarda as colunas
        for j in range(num_colunas): # executa dependedo do numero de colunas
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: ")) # O str e apenas para converter o inteiro em string, isso e meramente para mostrar ao usuario qual posição ele esta adicionando 
            linha.append(valor) # adiciona o valor escolhido pelo usuario na coluna 

        # adiciona linha á matriz
        matriz.append(linha) # acabou a coluna vai para proxima linha e reinicia
    return matriz   

def le_matriz():
    lin = int(input("Digite o numedo de linhas da matriz: "))
    col = int(input("Digite o numedo de colunas da matriz: "))
    imprime = cria_matriz(lin,col)
    organiza(imprime)

def organiza(matrix):
    print(matrix)
