#Logica para fatorial sem a função factorial fica assim:
# while(n>1) fat = fat * n ------ n = n - 1 ----- return fat

import math

def coe_bin(n, p):
    result = math.factorial(n) / (math.factorial(n - p)* math.factorial(p))
    return result


print(coe_bin(5, 3))

if coe_bin == n:
    print ("É isso ai valores iguais geralmente da 1")

if coe_bin(n, 1) == 1:
    print("É isso ai, quando fazemos coeficientes e o p vale 1 o resultado e sempre 1 o mesmo vale para zero")