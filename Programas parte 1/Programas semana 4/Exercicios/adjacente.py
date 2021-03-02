#Dado um numero ver se ele tem numeros adjacentes iguais

valor_user = input("Digite um numero inteiro:")

valor_cont = len(valor_user)

adjacente = False

auxiliar1 = 0
auxiliar2 = 0

while not adjacente:
    auxiliar1 = int(valor_user) // (10**(valor_cont - 1))
    valor_user = int(valor_user) % (10**(valor_cont - 1))
    valor_cont = valor_cont - 1
    auxiliar2 = valor_user // (10**(valor_cont - 1))
    if auxiliar1 == auxiliar2 and valor_cont > 0:
        adjacente = True
        print("sim")
    elif valor_cont == 0:
        adjacente = True
        print("não")