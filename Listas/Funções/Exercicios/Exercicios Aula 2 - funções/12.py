# Crie uma função que receba uma lista
# como argumento, os valores da lista devem ser
# numéricos, por fim retorne a média desses
# valores.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def media(lista):
    return sum(lista) / len(lista)

resultado = media(numeros)

print(resultado)