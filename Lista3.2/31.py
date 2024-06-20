# Um  funcionário  recebe  aumento  anual.  Em  2019  foi  contratado  por  4000  reais.  Em  2020 
# recebeu aumento de 1.5%. A partir de  2021, os aumentos sempre correspondem ao dobro do 
# ano anterior. Faça um programa que determine o salário atual do funcionário. 


salario2019 = 4000

print(f"Salario em 2020: R%{salario2019 * 1.015:.2f}")

salario2021 = salario2019 * 1015

anoAtual= int(input("Digite o ano atual: "))

aumento = 1.015
i =0
while(i < anoAtual):
    aumento = (0.015 * 2 ) + 1
    print(f"Salario no ano de {anoAtual+1}: ")
    i += 1