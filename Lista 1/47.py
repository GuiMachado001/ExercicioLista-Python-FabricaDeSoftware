# 47. Uma Indústria de Peças automotivas paga R$32,50 por hora normal trabalhada, e R$44,50 por
# hora extra. Faça um algoritmo que leia a quantidade de horas normais trabalhas e a quantidade
# de horas extras. Calcule e imprima o salário bruto e o salário líquido de um determinado
# funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se 11%
# do INSS.



horasNormais = 32.50
horasExtra = 44.50

horasNormaisTrab = float(input("Digite a quantidade de horas normais trabalhadas: "))
horasExtraTrab = float(input("Digite a quantidade de horas extras trabalhadas: "))

ValorBruto = (horasNormaisTrab * horasNormais) + (horasExtraTrab + horasExtra)

ValorLiqui = ValorBruto * 0.89

print(f"O valor liquido a pagar é de R${ValorBruto} \nO valor liquido a pagar é de: R${ValorLiqui}")