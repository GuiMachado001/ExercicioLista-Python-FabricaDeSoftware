#  Classe Livro: Crie uma classe que modele um Livro. Esta classe deve possuir os 
# seguintes atributos:
# - Nome
# - Autor
# - Editora
# - Páginas

# - A classe deve ter o seguintes métodos:
# - Alterar_editora()
# - Listar_qtde_paginas()
listaLivros = []

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
        print("\nLivro Cadastrado com Sucesso !!")
        return Livro(nome, autor, editora, pag)

    def alterarNome(self, novoNome):
        self.nome = novoNome
        print("\nNome Alterado com Sucesso!!")

    def alterarAutor(self, novoNomeAutor):
        self.autor = novoNomeAutor
        print("\nNome do autor Alterado com Sucesso!!")

    def alterarEditora(self, novoNomeEditora):
        self.editora = novoNomeEditora
        print("\nNome da esitora Alterado com Sucesso!!")
    
    def alterarQuantPaginas(self, quantidadePag):
        self.pag = quantidadePag
        print("\nquantidade de paginas Alterada com Sucesso!!")


    def listarLivros(listaLivros):
        for i, livro in enumerate(listaLivros):
            print(f"{i} - Nome: {livro.nome}, Autor: {livro.autor}, Editora: {livro.editora}, Páginas: {livro.pag}")


def menu():
    print()
    print("#"*30)
    print("Digite a Opção")
    print(" 1-Cadastrar Livro \n 2-Alterar Nome \n 3-Alterar Autor \n 4-Alterar Editora \n 5-Alterar qunatidade de paginas \n 6-Listar Livros Cadastrados")


livro1 = Livro('teste', 'guilherme', 'saraiva', 12)
listaLivros.append(livro1)

while True:
    menu()
    opcao = int(input("--> "))

    if (opcao  == 1):
        livro = Livro.cadastrarLivro()
        listaLivros.append(livro)
        
    elif(opcao == 2):
        Livro.listarLivros(listaLivros)
        opcaoLivro = int(input("Qual livro deseja alterar? "))
        novoNome = input("Digite o novo nome do livro: ")
        listaLivros[opcaoLivro].alterarNome(novoNome)

    elif(opcao == 3):
        Livro.listarLivros(listaLivros)
        opcaoLivro = int(input("Qual livro deseja alterar? "))
        novoNomeAutor = input("Digite o novo nome do autor: ")
        listaLivros[opcaoLivro].alterarAutor(novoNomeAutor)

    elif(opcao == 4):
        Livro.listarLivros(listaLivros)
        opcaoLivro = int(input("Qual livro deseja alterar? "))
        novoNomeEditora = input("Digite o novo nome da editora: ")
        listaLivros[opcaoLivro].alterarEditora(novoNomeEditora)
    
    elif(opcao == 5):
        Livro.listarLivros(listaLivros)
        opcaoLivro = int(input("Qual livro deseja alterar? "))
        qunatidadePaginas = input("Digite a quantidade de paginas: ")
        listaLivros[opcaoLivro].alterarQuantPaginas(qunatidadePaginas)

    elif(opcao == 6):
        Livro.listarLivros(listaLivros)
    
    else:
        print("Opção inválida!!")