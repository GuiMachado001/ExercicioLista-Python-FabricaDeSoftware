# Crie uma função que armazene os dados de uma pessoa em um
# dicionário e imprima-os na tela, Utilize argumentos nomeados **kwargs,
# exemplo de saída:

def usuario(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} is {value}")

nomeCompleto = input("Digite seu nome e sobrenome: ")
nome, sobrenome = nomeCompleto.split()

email = input("Digite seu E-mail: ")
pais = input("Digite seu país: ")
idade = int(input("Digite sua idade: "))
telefone = int(input("Digite seu numero de telefone: "))

usuario(firstname = nome, lastname = sobrenome, email = email, pais = pais, idade = idade, telefone = telefone)