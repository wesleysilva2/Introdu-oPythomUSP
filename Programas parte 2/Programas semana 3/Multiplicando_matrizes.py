def multiplicaveis(matriz1, matriz2): # E a multiplicação das linhas de matriz 1 pelas colunas de matriz 2
    multiplicacao = []
    mult_linhas_mat1 = len(matriz1) # Conta a quantidade de linhas 
    mult_colunas_mat1 = len(matriz1[0]) # Conta a quantidade de colunas
    mult_linhas_mat2 = len(matriz2) 
    mult_colunas_mat2 = len(matriz2[0]) 

    if mult_colunas_mat1 != mult_linhas_mat2:
        return False
    

    for linha in range(mult_linhas_mat1): #Começando uma nova linha 
        multiplicacao.append([])
        for coluna in range(mult_colunas_mat2): # Adicionando uma nova coluna na linha
           multiplicacao[linha].append(0) # Inicializa com 0 q e elemento neutro, para a partir dai fazer uma soma acumulativa das multiplicações de linhas por colunas
           for x in range(mult_colunas_mat1):
               multiplicacao[linha][coluna] += matriz1[linha][x] * matriz2[x][coluna] 

               # O resultado da soma dos resultados de multiplicação de uma linha inteira por uma coluna inteira e depositado na matriz resultante(multiplicacao) 
           
    return multiplicacao  


if __name__ == '__main__':
    matriz1 = [[1,2,3],[4,5,6]]
    matriz2 = [[1,2],[3,4],[5,6]]
    print(multiplicaveis(matriz1,matriz2))
