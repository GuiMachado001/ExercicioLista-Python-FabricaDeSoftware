#Verificar se o ano é Bissexto

quantDias = int(input("Digite a quantidade de dias do ano atual: "))


if(quantDias > 365):
    print("O ano é Bissexto")
else:
    print("O ano não é bissexto")