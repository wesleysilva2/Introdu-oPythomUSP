import math

cordenada_x1 = float(input("Digite a primeira cordenada do plano cartesiano:"))
cordenada_y1 = float(input("Digite a segunda cordenada do plano cartesiano:"))
cordenada_x2 = float(input("Digite a terceita cordenada do plano cartesiano:"))
cordenada_y2 = float(input("Digite a quarta cordenada do plano cartesiano:"))

distancia_pontos_catesiano = math.sqrt((cordenada_x1 - cordenada_x2)**2 + (cordenada_y1 - cordenada_y2)**2)

if (distancia_pontos_catesiano >= 10):
    print("longe")
else:
    print("perto")