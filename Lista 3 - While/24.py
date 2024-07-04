# Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3
# ou 5.

cont = 0
soma = 0

while(cont < 1000):
    if(cont % 3 == 0 or cont % 5 == 0):
        soma += cont
        cont += 1
    else:
        cont+=1

print(soma)