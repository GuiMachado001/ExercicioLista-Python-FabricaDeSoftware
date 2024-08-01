# Crie uma função que receba dois números como parâmetros e mostre a potência do número
# elevado a n vezes, exemplo:
# pot(2,3)
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8

def potencia(base, expoente):
    i = 1
    while(i <= expoente):
        print( f"{base} ** {i} = {base ** i}")
        i += 1


base = int(input("Digite um numero inteiro para a base: "))
expoente = int(input("Digite um numero inteiro para o expoente: "))

expo = potencia(base, expoente)

print(expo)