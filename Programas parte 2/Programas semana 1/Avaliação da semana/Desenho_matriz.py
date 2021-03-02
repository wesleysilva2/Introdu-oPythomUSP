def imprime_matriz(matriz):
    
    conta_linhas = len(matriz)
    conta_colunas = len(matriz[0]) 
    for x in range(conta_linhas): 
        if x > 0: # esse if e para que a partir da segunda linha ele comece a pular, ele organiza em matriz 
            print(end="\n")
            
        for j in range(conta_colunas):
            seletor_posicao = matriz[x][j] # com a matriz assim ele pega um valor por vez na matriz e vai printando em baixo
            if j == conta_linhas:
                print(seletor_posicao,end="")
            else:
                print(seletor_posicao,end=" ")# end no final para ter um espaço entre os valores e que eles não quebrem a linha 
        
