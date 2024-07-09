# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

lista = []
i =0

while( i < 10):
    num = int(input("Digite um numero inteiro: "))
    lista.append(num)
    i+=1

print(f"Maior numero: {max(lista)} \nMenor número: {min(lista)}")