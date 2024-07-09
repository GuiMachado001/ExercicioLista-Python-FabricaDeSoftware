#  Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda 
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno 
# foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos

nota1 = float(input("Digte a nota da primeira prova: "))
nota2 = float(input("Digte a nota da segunda prova: "))
nota3 = float(input("Digte a nota da terceira prova: "))

mediaPonde = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 1 +2 )

if(mediaPonde > 6 ):
    print(f"A média do aluno é de {mediaPonde}: APROVADO")
else:
    print(f"A média do aluno é de {mediaPonde}: REPROVADO")