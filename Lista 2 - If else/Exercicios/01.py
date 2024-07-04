#Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre: o produto do primeiro 
#com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número
#digitado ao cubo

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
real1 = float(input("Digite um numero real: "))

res1 = num1 * (num2 / 2)

res2 = (num1 * 3) + real1

res3 = real1 ** 3

print(f"O produto do primeiro com a metade do segundo: {res1}")
print(f"A soma do triplo do primeiro com o terceiro: {res2}")
print(f"O terceiro número digitado ao cubo: {res3}")