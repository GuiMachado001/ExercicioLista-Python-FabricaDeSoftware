# 33. Sejam a e b os catetos de um triâ ngulo, onde a hipotenusa e obtida pela equação:
# ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √ 𝑎^2 + 𝑏^2
# Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa e imprima o
# resultado dessa operação


import math

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))

hipotenusa = (valorA * valorA) + (valorB * valorB)

raizQuadrada = math.sqrt(hipotenusa)

print("O valor da hipotenusa é: ",raizQuadrada)