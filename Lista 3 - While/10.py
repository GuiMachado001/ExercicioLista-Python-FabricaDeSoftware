# Crie um programa que leia um número inteiro N e depois imprima os N primeiros números
# naturais ímpares

i = 0
while(True):
    num = int(input("Digite um numero inteiro: "))

    if(num <= 0):
        print("Numero inválido")

    else:
        while(i < 5):
            if(num % 2 == 0):
                num -= 1
            else:
                print(f"{num} - Impar")
                num -= 1
                i += 1
        
        