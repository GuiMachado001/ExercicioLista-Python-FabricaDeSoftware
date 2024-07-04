# Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para
# resolver o problema utilize estrutura de repetição.


flag = True
while(flag):
    base = int(input("Digite o valor da Base: "))
    expoente = int(input("Digite o valor do Expoente: "))

    resultado = 0
    if(expoente == 0):
        print("O resultado é: 1")
    elif(expoente == 1):
        print(f"O resultado é: {base}")
    else:
        resultado = base ** expoente
        print(resultado)