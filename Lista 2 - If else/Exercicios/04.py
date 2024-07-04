# Crie um programa que receba três números e mostre-os se estão em ordem crescente.

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
num3 = int(input("Digite outro numero inteiro: "))

if(num1 < num2 and num3 > num2):
    print(f"Estão em dordem crescente: num1: {num1}, num2: {num2}, num3: {num3}")
else:
    print("Não estão em ordem crescente!")