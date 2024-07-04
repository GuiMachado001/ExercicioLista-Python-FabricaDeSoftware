idade = int(input("Digite a idade do aluno: "))

if(idade >= 18):
    print("Tem idade para tirar CNH")

    teste_psicotecnico = input("Digite se o aluno esta 'APROVADO' ou 'REPROVADO': ")

    prova_teorica = int(input("Digite a nota do aluno: "))

    if(teste_psicotecnico == "APROVADO" and prova_teorica >= 7):
        print("Está apto para fazer as aulas práticas!")
        
    elif(teste_psicotecnico == "REPROVADO" or prova_teorica < 7):
        print("Não está apto para fazer as aulas práticas!")
else:
    print("Não tem idade para tirar CNH")