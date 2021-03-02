def dimensoes(matriz):
    contador_Linhas = len(matriz) # Calcular numero de linhas 
    contador_Colunas = len(matriz[0]) # para calcular o numero de colunas pegamos uma das listas e contamos seus elementos 

    if len(matriz[0]) == 0: # verificando se a lista desta vazia 
        contador_Colunas = 0
         
    print(contador_Linhas,"X",contador_Colunas,sep="") # o sep e para deixar os valres bem juntinhos tipo em vez de 3 x 1 fica 3x1, ele remove o espaço padrão do phyton
    


