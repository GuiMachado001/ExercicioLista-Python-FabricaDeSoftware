# Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números 
# forem iguais, imprima a mensagem: Números iguais.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))

if(num1 > num2):
    print(f"O numero {num1} é maior que {num2}")
elif(num2 > num1):
    print(f"O numero {num2} é maior que {num1}")
else:
    print("Os números são Iguais!")