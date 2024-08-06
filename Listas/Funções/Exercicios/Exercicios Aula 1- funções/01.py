# Crie uma função que necessite de três
# argumentos, e que imprima o produto desses
# três argumentos.

def somar(x,y,z):
    res = x + y + z
    return res

valor = input("Digite o valor de X, Y e Z (formato: x, y, z): ")
x, y,z = valor.split(',')

x = int(x)
y = int(y)
z = int(z)

resposta = somar(x, y, z)

print(f"A soma de {x} + {y} + {z} é de {resposta}")