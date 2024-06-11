# Escreva um programa que leia 10 inteiros e imprima sua média

lista= []
i=0
while(i<10):
    num = int(input("Digite um numero inteiro: "))
    lista.append(num)
    i += 1

media = sum(lista) / 10

print(media)