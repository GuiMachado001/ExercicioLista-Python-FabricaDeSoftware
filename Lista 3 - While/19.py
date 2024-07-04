# Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um
# dos algarismos que compõem o número.

flag = True
i = 0

while(flag):
    num = int(input(("Digite um numero entre 100 e 9999: ")))

    if(num >= 100 and num <= 9999):
        numString = str(num)
        while(i < len(numString)):
            print(f"Algarismo {i} = {numString[i]}")
            i+= 1


    else:
        print("Numero inválido... Digite um número entre 100 e 9999")