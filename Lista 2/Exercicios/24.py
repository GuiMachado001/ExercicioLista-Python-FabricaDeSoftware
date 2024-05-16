# Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:

baseMaior = float(input("Digite o valor da base Maior: "))
baseMenor = float(input("Digite o valor da base Menor: "))
altura = float(input("Digite o valor da altura: "))

area = ((baseMaior + baseMenor) * altura) / 2


if(baseMaior > 0 and baseMenor > 0): 
    print(f"A área do trapézio é: {area}cm")
else:
    print("O valor da base Maior e da Base Menor deve ser maior que zero")