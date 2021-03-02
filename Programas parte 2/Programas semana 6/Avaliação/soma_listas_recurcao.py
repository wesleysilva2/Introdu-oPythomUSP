def soma_lista(lista): # Somar todos os elementos da lista e devolver a soma
    
    quantidade_base = len(lista)
    
    if quantidade_base <= 1: # Base da recurcao 
        return lista[0]
    
    chave_para_unico = False
    return lista[0] + soma_lista(lista[1:])
  
    

    
        

    
    
    
