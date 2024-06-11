# Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os
# números ímpares de 1 até N em ordem crescente.

flag = True
i = 0
while(flag):
    num = int(input("Digite um numero inteiro ímpar: "))

    if(num % 2 != 0):
        print("Número inválido... Digite um numero ímpar")
    else:
        while(i <= num):
            if(i % 2 != 0 ):
                print(i)
                i += 1
            else:
                i += 1