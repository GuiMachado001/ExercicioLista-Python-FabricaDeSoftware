# 49. A fábrica de refrigerantes Frutuba vende seu produto em três formatos: lata de 350 ml,
# garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
# quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele
# comprou.


quantLata = int(input("Digite a quntidade de latas a se comprar: "))
quantGarraf1 = int(input("Digite a quntidade de garrafas de 600ml a se comprar: "))
quantGarraf2 = int(input("Digite a quntidade de garrafas de 2l a se comprar: "))

litrosLata = (quantLata * 350) / 1000
litrosGarraf1 = (quantGarraf1 * 600) / 1000
litrosGarraf2 = (quantGarraf2 * 2)

print(f"A quantidade em Litros de cada refrigerante é: \nLata: {litrosLata}L \nGarrafa 600ml: {litrosGarraf1}L \nGarrafa 2l: {litrosGarraf2}L")