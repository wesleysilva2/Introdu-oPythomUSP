def ePrimo(n):
    fator = 2
    while(n % fator != 0 and fator < n/2): # se ate n sobre 2 vc n encontrou um divisor então n vai encontrar mais
        fator = fator + 1
    if (n % fator == 0):
        return False
    else:
        return True

n = int(input("Digite um numero positivo:"))

while (n > 0):
    if ePrimo(n):
        print(n, "É primo")
    else:
        print(n, "Não é primo")
    n = int(input("Digite um numero positivo:"))