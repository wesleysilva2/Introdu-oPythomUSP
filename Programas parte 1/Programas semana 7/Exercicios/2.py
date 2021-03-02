def é_primo(x):
    fator = 2
    while fator * fator <= x:
        if x % fator == 0:
            return False
        fator = fator + 1
    return True
 
def n_primos(n):
    contagem_primos = 0
    for i in range(2, n + 1):
        if é_primo(i):
            contagem_primos = contagem_primos + 1
    return contagem_primos
 
# Teste
for t in range(0, 121):
    print("p(" + str(t) + ") = " + str(n_primos(t)))