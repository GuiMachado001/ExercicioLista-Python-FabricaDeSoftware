# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número 
# negativo. O programa tem que retornar o maior e o menor número lido. 

lista = []
while(True):
    num = int(input("Digite um numero inteiro ou um numero negativo para finalizar: "))

    lista.append(num)

    if(num < 0):
        break

print(f"Maior numero {max(lista)} \nMenor numero {min(lista)}")