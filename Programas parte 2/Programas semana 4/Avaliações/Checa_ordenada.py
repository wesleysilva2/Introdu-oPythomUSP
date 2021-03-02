def ordenada(lista):
    
    fim_checagem = len(lista)
    checa = 0 
    
    for i in range(fim_checagem - 1):
        
        posicao_minimo = i

        for j in range(i+1, fim_checagem):
            if lista[j] < lista[posicao_minimo]: # Checando se os valores depois do posicao_minimo são maiores que ele
                checa = 1
        
    if checa == 1:
        return False
    else:
        return True    

         
