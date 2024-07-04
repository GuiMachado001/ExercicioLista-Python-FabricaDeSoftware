#Verificar se um numero está dentro de um intervalo específico

num1 = int(input("Por favor insira o número inicial: "))
num2 = int(input("Por favor digite o número final: "))

numVerif = int(input("Por favor digite o número a ser verificado: "))

if(numVerif >= num1 and numVerif <= num2):
    print(f"o numero '{numVerif}' está dentro do intervalos")
else:
    print(f"O numero '{numVerif}' não esta dentro do intervalo")