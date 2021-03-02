import math

valor_a = float(input("Digite o valor de A da expressão:"))
valor_b = float(input("Digite o valor de B da expressão:"))
valor_c = float(input("Digite o valor de C da expressão:"))


Delta = (valor_b**2) - (4 * valor_a * valor_c)

if (Delta < 0):
    print("esta equação não possui raízes reais")

else:
    baskhara_positivo = (-valor_b + math.sqrt(Delta)) / (2 * valor_a)
    baskhara_negativa = (-valor_b - math.sqrt(Delta)) / (2 * valor_a)

    if (Delta == 0):
     baskhara_valor0 = -valor_b / (2 * valor_a)
     print("as raízes da equação são X e Y",baskhara_valor0)
    else:

        if (baskhara_positivo < baskhara_negativa):
            print("as raízes da equação são",baskhara_positivo,"e",baskhara_negativa)
        else:
            print("as raízes da equação são",baskhara_negativa,"e",baskhara_positivo)
