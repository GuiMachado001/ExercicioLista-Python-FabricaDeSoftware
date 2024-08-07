# Crie uma função que receba múltiplos
# argumentos não nomeados, considere que a
# função receba números inteiros como
# argumentos e retorne a soma dos argumentos.

def somar(*args):
    soma = sum(args)
    return soma


num = input("Insira os numeros que deseja somar (Formato: 2, 4, 6, 8): ")
valores = [int(x) for x in num.split(",")]

resultado = somar(*valores)
print(resultado)