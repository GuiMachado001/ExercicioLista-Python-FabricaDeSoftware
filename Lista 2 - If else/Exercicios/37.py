# O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do 
# distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, 
# de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
# CUSTO DE FÁBRICA % DO DISTRIBUIDOR % DOS IMPOSTOS
# até R$12.000,00 5 isento
# entre R$12.000,00 e 25.000,00 10 15
# acima de R$25.000,00 15 20


custoFabr = float(input("Digite o valor do custa da fábrica referente ao carro novo: R$"))

if(custoFabr < 12000.00):
    print(f"Custa da fábrica: R${custoFabr} \nComissão do Distribuidor: 5% \nCusto do Imposto: ISENTO \nValor Total: R${(custoFabr*0.05)+custoFabr}")
elif(12000.00 <= custoFabr <25000.00):
    print(f"Custa da fábrica: R${custoFabr} \nComissão do Distribuidor: 10% R${custoFabr*0.10} \nCusto do Imposto: 15% R${custoFabr*0.15} \nValor Total: R${((custoFabr*0.10)+ (custoFabr*0.15))+custoFabr}")
elif(custoFabr > 25000):
    print(f"Custa da fábrica: R${custoFabr} \nComissão do Distribuidor: 15% R${custoFabr*0.15} \nCusto do Imposto: 20% R${custoFabr*0.20} \nValor Total: R${((custoFabr*0.15)+ (custoFabr*0.20))+custoFabr}")