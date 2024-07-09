# Crie um programa que determine o mostre os 10 primeiros números pares, considerando 
# números maiores que 0

i = 0
while(True):
    try:
        num = int(input("Digite um numero inteiro: "))

        if(num <= 0):
            print("Numero inválido")

        else:
            while(i < 10):
                if(num % 2 == 0):
                    print(f"{num} - PAR")
                    num -= 1
                    i += 1
                else:
                    num -= 1
    except:
        print("Entrada inválida, Digite novamente")
            