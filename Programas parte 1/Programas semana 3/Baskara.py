import math

valor_a = float(input("Digite o valor de A da expressão: "))
valor_b = float(input("Digite o valor de B da expressão: "))
valor_c = float(input("Digite o valor de C da expressão: "))


Delta = (valor_b**2) - (4 * valor_a * valor_c)

if (Delta < 0):
    print("Esta raiz é menor que 0, portanto não possui numeros reais, favor digitar valores validos")
    print("Valor de Delta e:",Delta)

else:
    
    if (Delta == 0):
     baskhara_valor0 = -valor_b / (2 * valor_a)
     print("Tem uma unica soçução de sua conta de baskhara, pois o Delta é igual a 0 o resultado é:",baskhara_valor0)
    else:
     baskhara_positivo = (-valor_b + math.sqrt(Delta)) / (2 * valor_a)
     baskhara_negativa = (-valor_b - math.sqrt(Delta)) / (2 * valor_a)

     print("O valor positivo da sua conta de baskhara e:",baskhara_positivo,"E o valor negativo e:",baskhara_negativa)