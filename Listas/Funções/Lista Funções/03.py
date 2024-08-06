# Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor de
# retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

def posNegat (num):
    if(num == 0):
        return "0"
    elif(num > 0):
        return "1"
    else:
        return "-1"


while True:
    num = int(input("Digite um numero positivo ou negativo: "))

    verificar = posNegat(num)
    print(verificar)