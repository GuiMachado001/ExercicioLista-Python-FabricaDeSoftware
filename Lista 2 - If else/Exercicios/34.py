# Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e 
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a 
# segunda tabela).
# Preço antigo Percentual de aumento
# até R$ 50 5%
# entre R$ 50 e R$ 100 10%
# acima de R$ 100 15%

precAnt = float(input("Digite o valor atual do produto: R$"))

if(precAnt < 50):
    print(f"O precentual de aumento é de 5%, \nvalor do aument: R${precAnt*0.05} \nValor Total {precAnt+(precAnt*0.05)}")
elif(50 <= precAnt < 100):
    print(f"O precentual de aumento é de 10%, \nvalor do aument: R${precAnt*0.1} \nValor Total {precAnt+(precAnt*0.1)}")
elif(precAnt > 100):    
    print(f"O precentual de aumento é de 15%, \nvalor do aument: R${precAnt*0.15} \nValor Total {precAnt+(precAnt*0.15)}")