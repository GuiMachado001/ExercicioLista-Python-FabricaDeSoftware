# Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que 
# considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor 
# salário terão um aumento proporcionalmente maior do que os funcionários com um salário
# maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus
# adicional de salário. Crie um programa que leia:
# • o valor do salário atual do funcionário;
# • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na
# empresa)
# Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do 
# salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum 
# aumento.
# Salário Atual Reajuste (%) Tempo de Serviço Bônus
# Até 500,00 25% Abaixo de 1 ano Sem bônus
# Até 1000,00 20% De 1 a 3 anos 100,00
# Até 1500,00 15% De 4 a 6 anos 200,00
# Até 2000,00 10% De 7 a 10 anos 300,00
# Acima de 2000,00 Sem reajuste Mais de 10 anos 500,00

salarAtual = float(input("Digite o valor do salário atual do funcionário: R$"))
tempServ = float(input("Digite o tempo de serviço do funcionário em anos: "))

if(salarAtual == 500 or tempServ < 1):
    print(f"Reajuste de 25% e sem bônus \n{salarAtual} + 25% = {salarAtual*0.25}")
elif( 500 > salarAtual > 1000 or 1 <= tempServ <= 3 ):
    print(f"Reajuste de 20% e Bônus de R$100 \n{salarAtual} + 20%  + R$100 = {(salarAtual*0.20)+100}")
elif(1000 < salarAtual <= 1500 or 4 <= tempServ <= 6):
    print(f"Reajuste de 15% e Bônus de R$200 \n{salarAtual} + 15%  + R$200 = {(salarAtual*0.15)+200}")
elif(1500 < salarAtual <= 2000 or 7 <= tempServ <= 10):
    print(f"Reajuste de 10% e Bônus de R$300 \n{salarAtual} + 15%  + R$300 = {(salarAtual*0.15)+300}")
elif(salarAtual > 2000 or tempServ > 10):
    print(f"Sem reajuste e Bônus de R$500 \n{salarAtual} + R$500 = {salarAtual+200}")
    