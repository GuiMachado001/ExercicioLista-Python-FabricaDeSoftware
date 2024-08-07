#  Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os 
# seguintes atributos:
# - Nome
# - Autor
# - Editora
# - Páginas

# - A classe deve ter o seguintes métodos:
# - Alterar_editora()
# - Listar_qtde_paginas()
livros = []

class Livro:
    def __init__(self, nome, autor, editora, pag):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.pag = pag
    
    def cadastrarLivro():
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do Autor: ")
        editora = input("Digiteo nome da editora: ")
        pag = int(input("Digite a quantidade de paginas: "))
        return Livro(nome, autor, editora, pag)
    
    def alterarNome(livros):
        cont = 0
        for i in livros:
            print(f"{cont} - {i}")
            cont +=1
        opcaoLivro = int(input("Qual Livro deseja alterar? "))
        novoNome = input("Digite o novo nome do livro: ")
        livros[opcaoLivro].nome = novoNome
        

    def alterarEditora(self):
        alteracao = input("Digite a editora: ")
        self.editora = alteracao
    
    def listarQuantPag(self):
        print(f"Quantidade de paginas: {self.pag}")

    def listarLisvros(livros):
        for i in livros:
            print(i)


def menu():
    print("#"*30)
    print("Digite a Opção")
    print(" 1- Cadastrar Livro \n 2-Alterar Nome \n 3-Alterar Autor \n 4-Alterar Editora \n 5- Alterar qunatidade de paginas \n 6-Listar Livros Cadastrados")



livro1 = Livro('teste', 'guilherme', 'saraiva', '12')
livros.append(livro1.nome)

while True:
    menu()
    opcao = int(input())

    if (opcao  == 1):
        livro = Livro.cadastrarLivro()
        livros.append(livro.nome)
    elif(opcao == 2):
        Livro.alterarNome(livros)
    elif(opcao == 6):
        Livro.listarLisvros(livros)