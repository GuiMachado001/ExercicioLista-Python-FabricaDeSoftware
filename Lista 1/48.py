# A granja Frangofit possui um controle automatizado de cada frango da sua produção. No pé
# direito do frango há um anel com um chip de identificação; no pé esquerdo são dois
# anéis para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa
# R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja
# para marcar todos os seus frangos.



quantFrango = int(input("Digite a quantidade de frangos na granja"))

peDir = 4
peEsq = 3.50 * 2

totalGasto = (quantFrango * peDir) + (quantFrango * peEsq)

print(f"O total de gasto da granja para marcar todos os frangos é de R${totalGasto}")