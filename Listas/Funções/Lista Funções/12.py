# Elabore uma função que receba dois números inteiros positivos por parâmetros e retorne a 
# soma dos N números inteiros existentes entre eles. 
lista = []

def soma(num1, num2):
    for i in range(num1, num2):
        lista.append(i)
    print(f"A soma do numeros inteiros entre {num1} e {num2} é {sum(lista)}")

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

soma(num1, num2)