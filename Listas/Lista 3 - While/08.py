# Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
# média

lista = []
i = 0

while(i < 10):
    num = int(input("Digite um numero inteiro: "))

    if(num % 2 == 0):
        lista.append(num)
        i+=1
    else:
        i+=1

media = sum(lista) / 10

print(media)