def soma_matrizes(matriz1, matriz2):
    soma = []
    soma_linhas = len(matriz1) # Conta a quantidade de linhas 
    soma_colunas = len(matriz1[0]) # Conta a quantidade de colunas
    
    if len(matriz1[0]) != len(matriz2[0]) or len(matriz1) != len(matriz2):
        return False
    
    else:
        for j in range(soma_linhas): # percorre as linhas da matriz
            soma.append([]) # Cria uma nova matriz na linha soma, também cria o espaço onde a soma vai ocupar 
            for x in range(soma_colunas):
                operacao = matriz1[j][x] + matriz2[j][x] # Somando os valores que estão na mesma linha e coluna de listas diferentes 
                soma[j].append(operacao) # Adiciona o valor somado na posição que foi criada o escopo ou seja que foi adicionado anteriormente no ultimo append
        
        return soma   

if __name__ == "__main__": # Se vc rodar como script ele faz isso automatico, como script e no app do phyton e não no cmd
    matriz1 = [[1,2,3], [4,5,6], [7,8,9]]
    matriz2 = [[10,20,30], [40,50,60], [70,80,90]]
    print(soma_matrizes(matriz1, matriz2))
