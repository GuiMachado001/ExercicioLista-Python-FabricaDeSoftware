# Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou VVespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
# "Valor Inválido!", conforme o caso.

turno = input("Qual turno você estuda?? \nM - Matutino \nV - Vespertino \nN - Noturno \nTurno:  ")

if(turno =='M' or turno =='m'):
    print("Bom Dia!")
elif(turno =='V' or turno =='v'):
    print("Boa Tarde!")
elif(turno =='N' or turno =='n'):
    print("Boa Noite!")
else:
    print("Opção inválida")