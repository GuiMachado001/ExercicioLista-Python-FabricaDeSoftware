# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser
# informado o número de dados lidos e número de valores pares. O processo termina quando for
# digitado o número 0.

flag = True
contPar = 0
contLido = 0
parLista = []

while(flag):
    num = int(input("Digite um numero inteiro ou digite '0' para sair: "))

    if(num % 2 == 0 and num != 0):
        print("É par")
        parLista.append(num)
        contPar += 1
        contLido += 1
    elif(num % 2 != 0 and num != 0):
        print("É impar")
        contLido += 1
    elif(num == 0):
        print(f"Quantidade de numeros lidos: {contLido} \nQuantidade de numeros Pares: {contPar}")
        print(f"Numeros Pares Digitados: {parLista}")
        print("Programa Finalizado")
        flag = False
