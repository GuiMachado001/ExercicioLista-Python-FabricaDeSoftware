# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse
# número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

num = int(input("Digite um numero inteiro: "))

listaDivisiveis = []
cont = 1
while(cont < num):
    if(num % cont == 0):
        listaDivisiveis.append(cont)
        cont += 1

    else:
        cont += 1

print(f"Os numeros divisíveis por {num} são: {listaDivisiveis} \nA soma dos divisíveis equivale a: {sum(listaDivisiveis)}")