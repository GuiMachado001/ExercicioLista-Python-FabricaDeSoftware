# Faça um algoritmo que receba um número e apresente a tabuada do mesmo ao final;

num = int(input("digite um numero: "))

contador = 0

while(contador <= 10):
    print(f"{num} x {contador} = {contador * num}")
    contador += 1

