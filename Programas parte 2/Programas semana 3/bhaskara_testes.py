import math

# Este programa so devolve valores e não prints para facilitar os testes
# lembrar que sempre e mais interessante testar codigos que devolvem valores e não prints

class Bhaskara:
    
    def delta_calculo(self,valor_a, valor_b, valor_c):
        return (valor_b**2) - (4 * valor_a * valor_c)

    def main(self):
        valor_a = float(input("Digite o valor de A da expressão:"))
        valor_b = float(input("Digite o valor de B da expressão:"))
        valor_c = float(input("Digite o valor de C da expressão:"))
        print(self.calcula_raiz(valor_a, valor_b, valor_c))
        

    def calcula_raiz(self,valor_a,valor_b,valor_c):
        
        Delta = self.delta_calculo(valor_a,valor_b,valor_c)
        
        if (Delta < 0):
            return 0 
        else:
            baskhara_positivo = (-valor_b + math.sqrt(Delta)) / (2 * valor_a)
            baskhara_negativa = (-valor_b - math.sqrt(Delta)) / (2 * valor_a)

        if (Delta == 0):
         baskhara_valor0 = -valor_b / (2 * valor_a)
         return 1, baskhara_valor0
        else:

            if (baskhara_positivo < baskhara_negativa):
                return 2, baskhara_positivo, baskhara_negativa
            else:
                return 2, baskhara_negativa, baskhara_positivo

