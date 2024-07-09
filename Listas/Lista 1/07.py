# 7. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.


num1 = int(input("Digite um numero inteiro: "))

triplo = num1 * 3 + 1

dobro = num1 * 2 - 1

soma = triplo + dobro

print("A soma do sucessor do triplo de",num1, "com o antecessor de seu dobro é: ",soma)