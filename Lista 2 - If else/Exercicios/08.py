# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do 
# número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.


num = float(input("Digite o um numero: "))

if(num > 0):
    result = num * 0.5

    print(f"A raiz quadrada de {num} é {result}")
else:
    print("Seu número é inválido")