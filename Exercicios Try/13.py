# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando
# for informada a idade 0), e calcule a idade média desse grupo.


listaIdade = []
pessoa = 0

while(True):
    try: 
        idade = int(input(f"Digite a idade da pessoa {pessoa} ou digite '0' para finalizar: "))

        if(idade < 0):
            raise ValueError("Idade negativa não é permitida")
        
        elif(idade == 0):
            break
        else:
            listaIdade.append(idade)
        pessoa += 1

    except ValueError as e:
        print(f"Erro de execução: {e}")

        
media = sum(listaIdade) / len(listaIdade)

cont = 0
for i in listaIdade:
    print(f"Idade da pessoa {cont+1}: {listaIdade[cont]}")
    cont += 1

print(f"A media de idades é de: {media} anos")