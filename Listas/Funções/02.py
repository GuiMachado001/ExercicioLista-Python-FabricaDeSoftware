# Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência. Sendo
# base elevado ao expoente.

def exponenciacao(x, y):
    res = x ** y
    return res

valor = input("Digite o valor da base e do expoente (Formato: base, expoente): ")

base, expoente = valor.split(",")

base = int(base)
expoente = int(expoente)

resposta = exponenciacao(base, expoente)

print(f"O valor da exponenciação ente {base} e {expoente} é de: {resposta}")