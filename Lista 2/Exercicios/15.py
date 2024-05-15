# . Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela 
# a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, 
# onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o 
# programa termina.

nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))

if(nota1 >= 0.00 and nota2 >= 0.00 and nota1 < 10.00 and nota2 < 10.00):
    print(f"A média do aluno é {(nota1 + nota2)/2}")
else:
    print("Valor da nota invalido!")