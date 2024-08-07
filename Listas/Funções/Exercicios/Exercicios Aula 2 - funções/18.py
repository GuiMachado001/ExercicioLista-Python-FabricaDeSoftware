# Uma rede de churrascaria realiza promoções semanais e precisa
# automatizar os descontos de acordo com o dia da semana (terça-feira
# 10%, quarta-feira 15%, quinta-feira 20%). Crie uma função que calcule o
# preço final do consumo por pessoa. Considere a taxa de atendimento e o
# couvert, caso o cliente concorde com o pagamento. Utilize argumentos
# nomeados **kwargs, Exemplo de chamada da função:
# desconto(‘quinta-feira’,valor=99.90,taxa=0.10,couvert=15)


def desconto(dia,**kwargs):
    valorSemDesconto = kwargs.get("valor")
    taxa = kwargs.get("taxa")
    couvert = kwargs.get("couvert")

    valor10 = valorSemDesconto - (valorSemDesconto * 10/100)
    valor15 = valorSemDesconto - (valorSemDesconto * 15/100)
    valor20 = valorSemDesconto - (valorSemDesconto * 20/100)
    
    if(dia == 1 or dia == 5 or dia == 6 or dia == 7):
        print(f"Conta sem Taxa: {valorSemDesconto}")
        print(f"Conta com Taxa: {valorSemDesconto + taxa + couvert}")
    elif(dia == 2):
        print(f"Conta sem Taxa: {valor10:.2f}")
        print(f"Conta com Taxa: {valor10 + taxa + couvert}")
    elif(dia == 3):
        print(f"Conta sem Taxa: {valor15:.2f}")
        print(f"Conta com Taxa: {valor15 + taxa + couvert}")
    elif(dia == 4):
        print(f"Conta sem Taxa: {valor20:.2f}")
        print(f"Conta com Taxa: {valor20 + taxa + couvert}")



dia = int(input("Dia da Semana: \n 1-Segunda-Feira \n 2-Terça-Feira \n 3-Quarta-Feira \n 4-Quinta-Feira \n 5-Sexta-Feira \n 6-Sabado \n 7-Domingo \n"))

desconto(dia, valor=99.90, taxa=0.10, couvert=15)

