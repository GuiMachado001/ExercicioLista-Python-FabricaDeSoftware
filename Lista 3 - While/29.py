# Crie um programa que que leie um numero inteiro e calcule o menor número divisível por cada um dos números de 1 a 20?
# Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem
# sobrar resto.


num = int(input("Digite um numero inteiro: "))
numDivisiveis = []
i = 1

while(i <= 20):
    if(num % i == 0):
        numDivisiveis.append(i)
        i+=1
    else:
        i+=1

print(numDivisiveis)