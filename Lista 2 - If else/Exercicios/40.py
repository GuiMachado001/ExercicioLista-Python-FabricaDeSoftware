#  Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, Crie um programa que nos dê: 
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# IR (11%) INSS (8%) Sindicato (5 %)
# - Salário Bruto : R$
# - Salário Líquido: R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salario = float(input("Digite o valor do salário : R$"))
horasTrab = float(input("Digite as horas trabalhadas no mês: "))



print(f"Salario Bruto: R${salario} \nPagamento inss: R${salario*0.08} \nPagamento Sindicato: R${salario*0.05} \nSalario Liquido: R${salario-(salario*0.08)-(salario*0.05)}")