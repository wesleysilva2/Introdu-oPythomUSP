import math
valor_usuario = int(input("Digite o valor de n:"))

fatorial = 0

if (valor_usuario == 0):
    print(1)
else:
    fatorial = math.factorial(valor_usuario)
    print(fatorial)