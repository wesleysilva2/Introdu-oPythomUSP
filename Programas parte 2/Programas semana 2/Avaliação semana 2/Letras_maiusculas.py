def maiusculas (frase):

    resultado = ""

    for x in frase:
        valor_teste = ord(x)
        if valor_teste >= 65 and valor_teste <= 90:
            resultado = resultado + x
    return resultado
    
