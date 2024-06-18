# Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

A = int(input("Digite um numero inteiro: "))

B = A
i = 0
resultado = 1

while(i < B):
    resultado = resultado * A
    A -= 1
    i +=1

print(resultado)