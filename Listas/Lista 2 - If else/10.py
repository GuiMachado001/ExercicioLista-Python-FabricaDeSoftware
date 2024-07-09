# . Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
# • O número digitado ao quadrado;
# • A raiz quadrada do número digitado;

num = int(input("Digite um numero inteiro: "))

if(num > 0):
    print(f"{num} ao quadrado: ",num ** 2)
    print(f"A raiz de {num} é: ",num * 0.5)
else:
    print("Seu numero é negativo")