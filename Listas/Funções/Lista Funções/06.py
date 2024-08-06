# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
# Por exemplo: 127 -> 721.

def numReverso(num):
    numInvertido = num[::-1]
    print(f"Numero invertido: {numInvertido}")


num = input("Digite um numero: ")

numReverso(num)