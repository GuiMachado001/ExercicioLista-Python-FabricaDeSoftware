# 46. 4. A lanchonete do Gauchão vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias
# de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo
# ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo
# em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades
# (em quilos) de queijo, presunto e carne necessários para compra


queijo = 50
presunto = 50
carne = 100

quantSanduiche = int(input("Digite a quantidade de sanduiches que irá fazer: "))

quantQueijo = (quantSanduiche * queijo) / 1000 
quantPresunto = (quantSanduiche * presunto) / 1000 
quantCarne = (quantSanduiche * carne) / 1000 

print(f"A quantidade de cada item que deve comprar em Kg é: \nQueijo: {quantQueijo}Kg \nPresunto: {quantPresunto}Kg \nCarne: {quantCarne}Kg")