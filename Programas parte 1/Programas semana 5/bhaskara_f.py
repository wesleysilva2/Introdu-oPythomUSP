import math


def main():
    valor_a = float(input("Digite o valor de a:"))
    valor_b = float(input("Digite o valor de b:"))
    valor_c = float(input("Digite o valor de c:"))
    print("O baskhara dessa raiz é:",baskhara(valor_a,valor_b,valor_c))


def baskhara (valor_a, valor_b, valor_c):
    Delta = (valor_b**2) - (4 * valor_a * valor_c)
    
    if (Delta < 0):
        return "esta equação não possui raízes reais"
        
    else:
        baskhara_positivo = (-valor_b + math.sqrt(Delta)) / (2 * valor_a)
        baskhara_negativa = (-valor_b - math.sqrt(Delta)) / (2 * valor_a)

        if (Delta == 0):
            baskhara_valor0 = -valor_b / (2 * valor_a)
            return baskhara_valor0
        else:
            if (baskhara_positivo < baskhara_negativa):
                return baskhara_positivo, baskhara_negativa
            else:
                return baskhara_negativa, baskhara_positivo
