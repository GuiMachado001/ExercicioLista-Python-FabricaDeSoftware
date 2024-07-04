# Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número 
# fornecido é primo ou não

i = 2
while(True):
    num = int(input("Digite um numero inteiro: "))
    
    if(num > 3):
        while(True):
            if(num % 2 == 0 or num % 3 == 0):
                print(f"Numero não é primo")
                break
            else:
                print("Numero Primo")
                break
    elif(num == 0):
        print("O numero é 0, por favor digite outro numero")
    elif(num == 1):
        print("O numero é 1, por favor digite outro numero")
    elif(num == 2):
        print("O numero é primo")
    elif(num == 3):
        print("O numero é primo")
    else:
        print("O numero é negativo, por favor digite um numero positivo")