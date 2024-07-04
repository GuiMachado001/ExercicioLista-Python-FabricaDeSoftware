# Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas 
# com os valores invertidos.
try:
    num1 = int(input("Digite um número inteiro: "))
    num2 = int(input("Digite um número inteiro: "))

    num1, num2 = num2, num1
    print(f"num1: {num1} \nnum2: {num2}")
except:
    print("Erro: Entrada inválida! por favor, digite um número.")