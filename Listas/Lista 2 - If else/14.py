# Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem 
# crescente. Caso contrário, imprima não está em ordem crescente.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = int(input("Digite um número inteiro: "))

if(num1 < num2 and num2 < num3):
    print("Crescente")
else:
    print("Não está em ordem crescente")