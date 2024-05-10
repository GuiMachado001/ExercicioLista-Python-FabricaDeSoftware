#Determinar se é ano de eleição

anoAtual = int(input("Por favor digite o ano atual: "))

if(anoAtual % 4 == 0):
    print(f"O ano de {anoAtual} é ano de eleição!!")
else:
    print(f"O ano de {anoAtual} não é ano de eleição")