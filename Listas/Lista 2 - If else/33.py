# Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e 
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a 
# cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
# abaixo:
# Especificação Código Preço
# Hot Dog 100 12.00
# X-Salada 102 18.50
# X-BACON 103 25.50
# X-Burguer 104 17.00
# Suco de Laranja 105 9.50
# Refrigerante 106 6.00

codigo = int(input("Digite o código do produto: \n Hot Dog - código: 100 \n X-Salada - código: 102 \n X-BACON - código: 103  \n X-Burguer - código: 104  \n Suco de Laranja - código: 105  \n Refrigerante - código: 106 \nCódigo: "))

quant = int(input("Digite a quantidade do produto: "))

if(codigo == 100):
    print(f"Hod Dog: {quant} valor total: {quant*12}")
elif(codigo == 102):
    print(f"X-Salada: {quant} valor total: {quant*18.50}")
elif(codigo == 103):
    print(f"X-BACON: {quant} valor total: {quant*25.50}")
elif(codigo == 104):
    print(f"X-Burguer: {quant} valor total: {quant*17}")
elif(codigo == 105):
    print(f"Suco de Laranja: {quant} valor total: {quant*9.50}")
elif(codigo == 106):
    print(f"Refrigerante: {quant} valor total: {quant*6}")