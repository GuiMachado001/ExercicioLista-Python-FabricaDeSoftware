#  A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame 
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de 
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela 
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi 
# aprovado. Crie todas as verificações necessárias

notaLab = float(input("Digite a nota do trabalho de laboratório: "))
notaAvSemest = float(input("Digite a nota da Avaliação Semestral: "))
notaAvFinal = float(input("Digite a nota da Avaliação Final: "))

mediaPonde = ((notaLab * 1) + (notaAvSemest * 1) + (notaAvFinal * 2)) / (1 + 1 +2 )

if(mediaPonde >= 0 or mediaPonde <= 2.9):
    print(f"Aluno reprovado! média: {mediaPonde}")
elif(mediaPonde >= 3 or mediaPonde <= 5.9):
    print(f"Aluno de recuperação! média: {mediaPonde}")
else:
    print(f"Aluno aprovado! média: {mediaPonde}")