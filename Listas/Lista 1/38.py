# 38. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o
# número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga,
# sabendo-se que são descontados 8% para imposto de renda.


diasTrabalhados = int(input("Dias trabalhados do encanador: "))

diaria = 30

pagar = diasTrabalhados * diaria

totalPagar = pagar * 0.92

print("O valor a pagar com desconto é: ",totalPagar)

