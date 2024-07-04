# Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu 
# de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os 
# dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

escolha = int(input("Olá! \nEscolha uma opção: \n 1- Adição \n 2- Diferença entre os numeros \n 3- O produto entre os numeros \n 4- Divisão \n"))

num1 = int(input("Digite o valor de X: "))
num2 = int(input("Digite o valor de Y: "))

if(escolha == 1):
    print(f"Soma: {num1} + {num2} = {num1+num2}")
elif(escolha == 2):
    print(f"Diferença: {num1} - {num2} = {num1-num2}")
elif(escolha == 3):
    print(f"Produto: {num1} * {num2} = {num1*num2}")
elif(escolha == 4):
    print(f"Divisão: {num1} / {num2} = {num1 / num2}")
else:
    print("Opção inválida")
