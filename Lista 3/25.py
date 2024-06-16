# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando
# for informada a idade 0), e calcule a idade média desse grupo.

flag = True
listaIdade = []
pessoa = 0
while(flag):
    idade = int(input(f"Digite a idade da pessoa {pessoa} ou digite '0' para finalizar: "))

    if(idade == 0):
        flag = False
    else:
        listaIdade.append(idade)
    pessoa += 1


media = sum(listaIdade) / len(listaIdade)

cont = 0
for i in listaIdade:
    print(f"Idade da pessoa {cont+1}: {listaIdade[cont]}")
    cont += 1

print(f"A media de idades é de: {media} anos")