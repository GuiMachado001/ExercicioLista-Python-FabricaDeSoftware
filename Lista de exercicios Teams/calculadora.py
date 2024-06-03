# Um algoritmo para uma calculadora, o usuário digita o primeiro número, a 
# operação que deseja executar e o segundo número. Dependendo do que o usuário informar
# como operador, o algoritmo executará um cálculo diferente 
# (soma, subtração, multiplicação ou divisão).  



num1 = float(input("Digite o valor de A: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o valor de B: "))

def adicao(num1, num2):
    result = num1 + num2
    print(result)

def subtracao(num1, num2):
    result = num1 - num2
    print(result)

def multiplicacao(num1, num2):
    result = num1 * num2
    print(result)

def divisao(num1, num2):
    result = num1 / num2
    print(result)



if(operacao == '+'):
    adicao(num1, num2)

elif(operacao == '-'):
    subtracao(num1, num2)

elif(operacao == '*'):
    multiplicacao(num1, num2)

elif(operacao == '/'):
    divisao(num1, num2)