# Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a 
# tabela abaixo:
# IMC Classificação
# < 18,5 Abaixo do Peso
# 18,6 - 24,9 Saudável
# 25,0 - 29,9 Peso em excesso
# 30,0 - 34,9 Obesidade Grau I
# 35,0 - 39,9 Obesidade Grau II (severa)
# ≥ 40,0 Obesidade Grau III (mórbida)

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite sua altura em m: "))

imc = peso / (altura**2)

if(imc <= 18.5):
    print(f"Imc = {imc} Classificação: Abaixo do peso!")
elif(18.6 <= imc <= 24.9):
    print(f"Imc = {imc} Classificação: Saudável!")
elif(25.00 <= imc <= 29.9):
    print(f"Imc = {imc} Classificação: Peso em excsso!")
elif(30.00 <= imc <= 34.9):
    print(f"Imc = {imc} Classificação: Obesidade Grau I!")
elif(35.00 <= imc <= 39.9):
    print(f"Imc = {imc} Classificação: Obesidade Grau II (severa)!")
elif(imc >= 40.00):
    print(f"Imc = {imc} Classificação: Obesidade Grau (mórbida)II!")