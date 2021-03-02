# A função primeiro_lex(lista) que recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica. 

def primeiro_lex (lista_palavras):
    soma = 0
    auxiliar = 0 
    primeiro_passo = 1
    controlador = 0
    zerador = 0

    for y in lista_palavras:
        controlador = len(y)
        for x in y: # dois for um para pegar a palavra na lista e o outro para pegar letra por letra da palavra
            valor_lexicografico = ord(x) # vendo o valor lexicografico
            soma = soma + valor_lexicografico # somando o valor para ver quem tem o menor valor para ser o primeiro
            valor_lexicografico = 0
            zerador = zerador + 1 

        if soma > auxiliar or primeiro_passo == 1:
            auxiliar = soma
            menor_nome = y
            primeiro_passo = 0

        if zerador == controlador: # esse if serve apenas para quando acabar a palavra da vez o programa zere a soma para n interferir no proximo valor
                soma = 0
                zerador = 0 

        

    return menor_nome    
