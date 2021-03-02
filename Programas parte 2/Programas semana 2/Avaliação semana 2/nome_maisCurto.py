def menor_nome(lista_nomes):

    auxiliar = 0
    primeiro_passo = 1
    
    
    for x in lista_nomes:
        x = x.strip()
        x = x.capitalize() # organizando o nome, tirando os espaços(strip) e deixando so com uma letra maiuscula no começo
        conta_carac = len(x)
        if conta_carac < auxiliar or primeiro_passo == 1: # laço que checa se o nome atual analisado e menor ou maior que o anterior
            auxiliar = len(x) # coloquei apenas conta carac < auxiliar para ele pegar o primeiro menor que tiver
            menor_nome = x
            primeiro_passo = 0
            
    
    
    return menor_nome

    
    
