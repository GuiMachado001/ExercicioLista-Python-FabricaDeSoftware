# Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas 
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois 
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.

x = float(input("Por favor digite o valor de X: "))
y = float(input("Por favor digite o valor de Y: "))

operacao = float(input("Selecione a operação matemática: \n1-Adição \n2-Subtração \n3-Divisão \n4-Multiplicação \n"))

if(operacao == 1):
    print(f"A soma entre {x} e {y} é igual à: {x + y}")
elif(operacao == 2):
    print(f"A subtração entre {x} e {y} é igual à: {x - y}")
elif(operacao == 3):
    print(f"A divisão entre {x} e {y} é igual à: {x / y}")
elif(operacao == 4):
    print(f"A multiplicação entre {x} e {y} é igual à: {x * y}")
