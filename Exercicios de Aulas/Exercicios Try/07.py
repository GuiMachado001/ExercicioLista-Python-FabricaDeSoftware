# Escreva um programa que leia 10 inteiros e imprima sua média

lista= []
i=0
while(i<10):
    try:
        num = int(input("Digite um numero inteiro: "))
        lista.append(num)
        i += 1
    except:
        print("Entrada inválida, Digite novamente")
media = sum(lista) / 10

print(media)