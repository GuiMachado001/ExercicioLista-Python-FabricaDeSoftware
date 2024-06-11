# . Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A
# quantidade de números a serem lidos deve será fornecida pelo usuário.

quantNum = int(input("Digite a quntidade de numeros a serem inseridos: "))
lista = []
i = 0


while(i < quantNum):
    num = int(input("Digite um numero inteiro: "))
    lista.append(num)
    i+=1

print(max(lista))
