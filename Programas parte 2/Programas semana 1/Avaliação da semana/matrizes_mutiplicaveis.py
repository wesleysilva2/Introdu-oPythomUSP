def sao_multiplicaveis(matriz1, matriz2): # Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda
    conta_conlunas_1 = len(matriz1[0])
    conta_linhas_2 = len(matriz2)

    if conta_conlunas_1 == conta_linhas_2:
        return True
    else:
        return False