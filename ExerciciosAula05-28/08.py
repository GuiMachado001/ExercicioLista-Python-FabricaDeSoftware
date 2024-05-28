# Faça para 10 números inteiros para um vetor de inteiros. Computar um segundo vetor que
# terá o resultado da multiplicação por um escalar inteiro 5.

lista1 = [10, 2, 5, 4, 5, 6, 7, 8, 9, 10]
lista2 = []

i = 0

while(i < 5):
    mult = lista1[i]*5
    lista2.insert(i, mult)
    i += 1


print(lista1)
print(lista2)