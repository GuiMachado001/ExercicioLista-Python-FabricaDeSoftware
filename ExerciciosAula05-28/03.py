# Faça um algoritmo que receba 10 nomes em uma lista, e ao final apresente todos os nomes recebidos.


nomes = []
i = 0

while (i < 10):
    valor = input("Digite um nome a ser adicionado na lista: ")
    nomes.append(valor)
    i += 1

i2 = 0

while(len(nomes) > i2):
    print(nomes[i2])
    i2 += 1