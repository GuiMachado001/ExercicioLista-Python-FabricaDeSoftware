# Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
# de 0 até N em ordem decrescente.

num = int(input("Digite um numero inteiro: "))
i = 0
while(num >= i):
    print(num)
    num -= 1