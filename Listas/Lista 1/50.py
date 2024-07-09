# 50. DESAFIO – Utilize a fórmula de Euclides para Calcular a distância entre dois pontos:
# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder,
# respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos
# devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo
# plano. Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
# longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto.
# d(xy) = √(x1 - x2)^2 +(y1 - y2)^2

import math

coordX = float(input("Digite o valor da coordenada X: "))
coordY = float(input("Digite o valor da coordenada Y: "))

coordX2 = float(input("Digite o valor da coordenada X2: "))
coordY2 = float(input("Digite o valor da coordenada Y2: "))

form1 = (coordX - coordX2) * (coordX - coordX2)
form2 = (coordY - coordY2) * (coordY - coordY2)

somForm = form1 + form2

distancia = math.sqrt(somForm)

if(distancia >= 10):
    print("Longe na saida")

else:
    print("Perto da saida")


print(f"A distancia entre dos dois pontos cartesianos é de: {distancia}")