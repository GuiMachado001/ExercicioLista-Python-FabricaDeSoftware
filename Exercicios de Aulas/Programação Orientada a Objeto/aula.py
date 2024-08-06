## Classe pessoa
# Abstração do objeto pessoa na programação POO

## Atributos: nome, idade, email, cidade
# Métodos: Comer, dormir, estudar ( ações -> Funções -> Métodos)

class Pessoa:
    def __init__(self, nome, idade, email, cidade):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cidade = cidade

    def oi(self):
        print(f'Olá {self.nome}')

### Instanciar uma Classe

pes1 = Pessoa("Guilherme", 22, "teste@teste.com", "Campo Grande - MS")
# print(pes1.nome)
# print(pes1.idade)

pes2 = Pessoa("Maria", 52, "maria@gmail.com", "Rio de Janeiro")
# print(pes2.nome)
# print(pes2.idade)
pes2.oi()