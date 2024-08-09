# Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve possuir os 
# seguintes atributos:
#  Nome;
#  RA;
#  Nota 1, nota 2, nota 3, nota 4;

#  A classe deve ter o seguintes método:

#  Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final 
# é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado 
# somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5
# A situação será retornada a partir das notas obtidas pelo aluno.

listaAlunos = []

class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def cadastrarAluno():
        nome = input("Digite o nome do Aluno: ")
        ra = input("Digite a RA do aluno: ")
        nota1 = int(input("Digite a nota 1 do aluno: "))
        nota2 = int(input("Digite a nota 2 do aluno: "))
        nota3 = int(input("Digite a nota 3 do aluno: "))
        nota4 = int(input("Digite a nota 4 do aluno: "))
        print("\nAluno cadastrado com Sucesso !!")
        return Aluno(nome, ra, nota1, nota2, nota3, nota4)

    def alunosCadastrados(listaAlunos):
        for i, aluno in enumerate(listaAlunos):
            print(f"{i} - Nome: {aluno.nome}, RA: {aluno.ra}, Nota1: {aluno.nota1}, Nota2: {aluno.nota2}, Nota3: {aluno.nota3}, Nota4: {aluno.nota4}")

    def situacaoAluno(self):
        situacao = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if(situacao >= 7):
            print(f"Media: {situacao} O aluno se encontra Aprovado!")
        elif(situacao >= 5 and situacao <= 6.9):
            print(f"Media: {situacao} O aluno se encontra de Exame!")
        elif(situacao <5):
            print(f"Media: {situacao} O aluno se encontra Reprovado!")

    def alterarNota(self, novaNota1, novaNota2, novaNota3, novaNota4):
        self.nota1 = novaNota1
        self.nota2 = novaNota2
        self.nota3 = novaNota3
        self.nota4 = novaNota4
        print("\nNota alteradas com Sucesso !!")

def menu():
    print()
    print("#"*30)
    print("Digite a opção")
    print("1- Cadastrar Aluno")
    print("2- Listar alunos cadastrados")
    print("3- Mostrar situação do aluno")
    print("4- Alterar nota do Aluno")

while True:
    menu()
    opcao = int(input("-->"))

    if(opcao == 1):
        novoAluno = Aluno.cadastrarAluno()
        listaAlunos.append(novoAluno)

    elif(opcao == 2):
        Aluno.alunosCadastrados(listaAlunos)

    elif(opcao == 3):
        Aluno.alunosCadastrados(listaAlunos)
        opcaoAluno = int(input("Qual aluno deseja visualizar? "))
        listaAlunos[opcaoAluno].situacaoAluno()
    
    elif(opcao == 4):
        Aluno.alunosCadastrados(listaAlunos)
        opcaoAluno = int(input("Qual aluno deseja alterar? "))
        nota1 = input("Digite a nota 1 do aluno: ")
        nota2 = input("Digite a nota 2 do aluno: ")
        nota3 = input("Digite a nota 3 do aluno: ")
        nota4 = input("Digite a nota 4 do aluno: ")
        listaAlunos[opcaoAluno].alterarNota(nota1, nota2, nota3, nota4)