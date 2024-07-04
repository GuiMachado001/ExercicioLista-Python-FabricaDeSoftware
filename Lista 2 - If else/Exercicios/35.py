# Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao 
# vendedor. Para calcular a comissão, considere a tabela abaixo:
# Venda mensal Comissão
# Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
# Menor que R$20.000,00 R$400,00 +14% das vendas

valorVenda = float(input("Digite o valor da venda: R$"))

if(valorVenda >= 100000.00):
    print(f"A comissão é de R$700.00 + 16% do valor da venda \n16% de {valorVenda} = {valorVenda*0.16} \nTotal da comissão: R$700.00 + {valorVenda*0.16} = {valorVenda+700+(valorVenda*0.16)}")
elif(100000.00 > valorVenda >= 80000.00):
    print(f"A comissão é de R$650.00 + 14% do valor da venda \n14% de {valorVenda} = {valorVenda*0.14} \nTotal da comissão: R$650.00 + {valorVenda*0.14} = {valorVenda+650+(valorVenda*0.14)}")
elif(80000.00 > valorVenda >= 60000.00):
    print(f"A comissão é de R$600.00 + 14% do valor da venda \n14% de {valorVenda} = {valorVenda*0.14} \nTotal da comissão: R$600.00 + {valorVenda*0.14} = {valorVenda+600+(valorVenda*0.14)}")
elif(60000.00 > valorVenda >= 40000.00):
    print(f"A comissão é de R$550.00 + 14% do valor da venda \n14% de {valorVenda} = {valorVenda*0.14} \nTotal da comissão: R$550.00 + {valorVenda*0.14} = {valorVenda+550+(valorVenda*0.14)}")
elif(40000 > valorVenda >= 20000.00):
    print(f"A comissão é de R$500.00 + 14% do valor da venda \n14% de {valorVenda} = {valorVenda*0.14} \nTotal da comissão: R$500.00 + {valorVenda*0.14} = {valorVenda+500+(valorVenda*0.14)}")
elif(valorVenda < 20000.00):
    print(f"A comissão é de R$400.00 + 14% do valor da venda \n14% de {valorVenda} = {valorVenda*0.14} \nTotal da comissão: R$400.00 + {valorVenda*0.14} = {valorVenda+400+(valorVenda*0.14)}")
    