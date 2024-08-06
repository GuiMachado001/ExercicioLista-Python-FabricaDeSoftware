# Escreva um programa, com uma função que necessite de um argumento. A função retornar o valor de caractere ‘P’, se seu
# argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def postivoNegativo(numero):
    if(numero > 0):
        return "P"
    elif(numero < 0 ):
        return "N"
    else:
        return "Digite outro numero"
    

numero = int(input("Digite um numero: "))


print(postivoNegativo(numero))