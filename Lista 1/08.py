# 8. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade
# e do ano atual.

from datetime import date

data = date.today().year

idade = int(input("Digite sua idade: "))

anoNascimento = data - idade

print("Seu ano de nascimento é: ",anoNascimento)