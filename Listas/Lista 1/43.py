# 43. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto
# arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de
# poupança (10% do total arecadado). Você foi contratado para fazer os cálculos para o dono. Com
# base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular
# os dados solicitados


pao = 0.12
broa = 1.50

quantPao = int(input("Por favor digite a quantidade de Pãozinhio vendidas no dia: "))
quantBroa = int(input("Por favor digite a quantidade de broas vendidas no dia: "))

valorPao = quantPao * pao
valorBroa = quantBroa * broa

valorTotal = valorPao + valorBroa

valorPoup = valorTotal * 0.1
 
print(f"O valor de pão vendidos no dia é de R$ {valorPao} \nO valor de broa vendidas no dia é de R${valorBroa} \nO valor total de vendas é de R${valorTotal}")
print(f"O valor que deve guardar na poupança é de R${valorPoup}")
