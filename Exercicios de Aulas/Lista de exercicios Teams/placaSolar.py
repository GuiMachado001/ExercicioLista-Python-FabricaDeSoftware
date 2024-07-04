# 4- Calcular quantidade de painéis solares para uma residência. 

consumEnergia = float(input("Digite o consudo de energia da sua residência em kWh/m2: "))
energiaPainel = float(input("Qual a quantidade de energia gerada por um painel solar em kWh: "))

numPainel = consumEnergia / energiaPainel

print(f"A quantidade de painéis de energia necessários é de {numPainel} Paineis")