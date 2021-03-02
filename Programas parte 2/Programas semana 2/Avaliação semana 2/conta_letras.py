def conta_letras(frase, conta= "vogais"): # o conta = vogais e o padrão, se o usuario n digitar nada no lugar vai ser vogais

    frase = frase.lower() # Programa conta vogais ou consoantes da frase digitada pelo usuario, depedendo de sua escolha 
    conta_vogal = 0
    conta_consoantes = 0
    for x in frase:
        if conta == "vogais":
            if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
                conta_vogal = conta_vogal + 1
        elif conta == "consoantes":
            if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u' and x != ' ': # o com o espaço vazio e para ele cobrir o espaço em branco
                conta_consoantes = conta_consoantes + 1

    
    if conta == "vogais":
        return conta_vogal
    if conta == "consoantes":
        return conta_consoantes
