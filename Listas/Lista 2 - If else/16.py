# Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários 
# acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor 
# do seu salário líquido.

horaFunc = float(input("Digite a quantidade de horas do funcionário: "))

pagFunc = horaFunc * 40.50

if(pagFunc > 2500.00):
    valImpost = pagFunc * 0.11
    pagFunc = pagFunc - valImpost
    print(f"O valor a pagar ao funcionário é de {pagFunc}")
else:
    print(f"O valor a pagar ao funcionário é de {pagFunc}")
