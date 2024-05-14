# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim 
# como a diferença existente entre ambos.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

if(num1 > num2):
    print(f"O número {num1} é maior que {num2} com um diferentça de {num1 - num2} números")
else:
    print(f"O número {num2} é maior que {num1} com um diferentça de {num2 - num1} números")
