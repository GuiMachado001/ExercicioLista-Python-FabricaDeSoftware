# Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

menor = min(num1, num2)
maior = max(num1, num2)

contador = maior

par = 0
impar = 0

while(contador >= menor):
    if(contador %2 == 0):
        par += 1
    else:
        impar +=1
    contador -=1

print("Quantidade de números pares:", par)
print("Quantidade de números ímpares:", impar)
