# 41. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# • o total a pagar com desconto de 10%;
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# • a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)



valorLiq = float(input("Digite o valor liquido do produto: "))

valorComDesc = valorLiq * 0.9

valorParcela = valorLiq / 3

comissaoVista = valorComDesc * 0.05

comissaoParcela = valorLiq * 0.05

print("Valor com desconto: R$",valorComDesc, "\nValor por parcela em 3x: R$", valorParcela,"\nValor da comissão da venda a vista: R$",comissaoVista, "\nValor comissão da venda parcelada: R$",comissaoParcela)