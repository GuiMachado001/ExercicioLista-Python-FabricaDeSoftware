#Verificar se um numero é positivo, negativo ou zero

num = int(input("Digite um numero inteiro: "))

if(num > 0):
    print("Seu número é positivo")
elif(num < 0):
    print("Seu número é negativo")
elif(num == 0):
    print("Seu número é zero")