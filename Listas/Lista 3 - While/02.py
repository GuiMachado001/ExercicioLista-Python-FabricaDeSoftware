# Crie um programa que determine o mostre os 5 primeiros números ímpares, considerando 
# números maiores que 0

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
        
        