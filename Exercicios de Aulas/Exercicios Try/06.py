# Escreva um programa que peça ao usuário para digitar 10 valores e some-os

lista = []
i=0
while(i < 10 ):
    try:
        num = float(input("Digite um numero: "))
        lista.append(num)
        i += 1
    except:
        print("Entrada inválida, Digite novamente")
print(sum(lista))