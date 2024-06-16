# Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação.

flag = True

notasAluno = []

while(flag):
    nota = int(input("Digite a nota do aluno (0 a 10) ou digite '123' para finalizar: "))

    if(nota == 123):
        flag = False
    elif(nota < 0 or nota > 10):
        print("Nota inválida, favor insira uma nota de 0 a 10")
    else:
        print("Nota valida")
        notasAluno.append(nota)

cont = 0
for i in notasAluno:
    print(f"Nota Avaliação {cont+1}: {notasAluno[cont]}")
    cont += 1

media = sum(notasAluno) / len(notasAluno)

print(f"A média das notas do aluno é: {media}")