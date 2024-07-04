#Verificar se o num é divisivel por 3 ou 5

num = int(input("Por favor digite um numero inteiro: "))

if(num % 3 == 0 and num % 5 == 0):
    print(f"O numero {num} é divisivel por 3 e 5")
elif(num % 3 == 0):
    print(f"O numero {num} é divisivel por 3")
elif(num % 5 == 0):
    print(f"O numero {num} é divisivel por 5")
