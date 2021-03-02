meuCartao = int(input("Digite o numero do seu cartão: "))

cartãoLido = 1
encontreiMeuCartaoNaLista = False
while cartãoLido != 0  and not encontreiMeuCartaoNaLista:
    cartãoLido = int(input("Digite o numero do proximo cartão: "))
    if cartãoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
        
if encontreiMeuCartaoNaLista:
    print("Opa meu cartão esta na lista")
else:
    print("X, meu cartão não esta la")