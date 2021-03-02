def maior_primo(k): # pega um valor e retorna o maior primo abaixo dele
    if ( k % 2 != 0):
        return k
    elif (k % 2 == 0):
        return k - 1
    elif (k % 5 == 0):
        return k - 5
        
