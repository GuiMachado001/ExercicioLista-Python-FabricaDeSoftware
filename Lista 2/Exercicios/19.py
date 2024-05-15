# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma 
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se 
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”.

num = int(input("Digite um numero inteiro: "))

if(num > 0):
    n = str(num)
    print(f"Analisando o numero {format(num)}")
    n1 = int(n[0])
    n3 = int(n[1])
    n2 = int(n[2])

    print(f"{n1} + {n2} + {n3} = {n1 + n2 + n3}")
else:
    print("Número inválido")