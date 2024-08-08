# lasse Conta: Um banco mantém contas de clientes armazenando o número da conta, o 
# nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
# - Nome;
# - CPF;
# - Numero;
# - Saldo;
# A classe deve ter o seguintes métodos:
# - Depositar()
# - Sacar()  - OBS: somente enquanto a conta possuir saldo positivo
# - Imprimir saldo()

listaConta = []
listaAdministrador = []

class Conta:
    def __init__(self, nome, cpf, numero, senha, saldo=1000):
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def buscarUsuario(listaConta, entradaNome):
        for i, conta in enumerate(listaConta):
            if(conta.nome == entradaNome):
                return i
        return -1
    def buscarAdministrador(listaAdministrador):
        for i, conta in enumerate(listaAdministrador):
            if(conta.nome == entradaNome):
                return i
        return -1
    
    
    def setDepositar(deposito):
        listaConta[index].conta += deposito
        print("\nDepósito realizado com sucesso !!")

    def setSacar(self, saque):
        self.saldo -= saque
        print("\nSaque realizado com sucesso")

    def getMostrarSaldo(self):
        print(f"Saldo: R${self.saldo}")



def menuUsuario(nome):
    print(f"\n## Olá {nome} ##")

    print("Digite a opção")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Mostrar saldo")


def menuFuncionario(nome):
    print("ola", nome)
    print("#"*30)
    print("Digite a opção")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Mostrar saldo")
    print("4- Cadastrar Usuário")

admin = Conta('administrador', 11100033301, 6799999-9999, 'admin',100000)
admin2 = Conta('administrador2', 11100033301, 6799999-9999, 'admin2',100000)
listaAdministrador.append(admin)
listaAdministrador.append(admin2)

user1 = Conta('usuario1', 11100033301, 6799999-9999, 'user',100000)
user2 = Conta('usuario2', 11100033301, 6799999-9999, 'user2',100000)
listaConta.append(user1)
listaConta.append(user2)

while True:

    acesso = int(input("Você é um funcionario ou um usuário \n 1-Funcionario \n 2-Usuário \n--> "))

    if(acesso == 2):

        entradaNome = input("Olá, por favor, para entrar digite seu nome: ")
        index = Conta.buscarUsuario(listaConta, entradaNome)

        if(index != -1):
            while True:

                entradaSenha = input("Digite sua senha: ")
                if(entradaSenha == listaConta[index].senha):

                    menuUsuario(listaConta[index].nome)
                    opcao = int(input("-->"))

                    if(opcao == 1):
                        deposito = float(input("Digite o valor do deposito: "))
                        Conta.setDepositar(deposito)

                    elif(opcao == 2):
                        saque = float(input("Digite o valor do saque: "))
                        Conta.setSacar(saque)

                    elif(opcao == 3):
                        Conta.getMostrarSaldo()

                    else:
                        print("Opção invalida: ")

                else:
                    print("Senha Incorreta")
        else:
            print("Usuario não encontrado")



    if(acesso == 1):
        entradaNome = input("Olá, por favor, para entrar digite seu nome: ")
        index = Conta.buscarAdministrador(listaAdministrador, entradaNome)

        if(index != -1):
            while True:
                entradaSenha = input("Digite sua senha: ")

                if(entradaSenha == listaAdministrador[index].senha):
                    menuFuncionario(listaAdministrador[index].nome)
                    opcao = int(input("-->"))



                else:
                    print("Senha Incorreta")
        else:
            print("Usuario não encontrado")