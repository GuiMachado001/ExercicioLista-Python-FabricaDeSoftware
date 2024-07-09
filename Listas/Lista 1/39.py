# 39. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas
# no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.


ValorhoraTrab = float(input("Qual o valor da hora de trabalho em reais? "))
horasTrab = float(input("Qantas horas foram trabalhadas no mês? "))

valorPagar = (horasTrab * ValorhoraTrab) * 1.1

print(f"O valor a se pagar com os 10% adicionais é R$",valorPagar)