#Verificar se um numero é multiplo de 5 e 7 ao mesmo tempo.

num = int(input("Por favor digite um numero inteiro: "))

if(num % 35 == 0):
    print(f"{num} é divisivel por 5 e 7")
else:
    print(f"{num} não é divisivel por 5 ou 7")