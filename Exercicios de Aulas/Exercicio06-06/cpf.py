# Validar CPF
#     O cálculo do CPF é baseado nos 2 dígitos finais.
#     Para validar, pegue os nove primeiros dígitos do CPF, gere os dois
#     dígitos e salve em um novo CPF.
#     Compare se o CPF enviado é igual ao CPF gerado.
#     Se verdadeiro, o CPF é válido, caso contrário, inválido.

# * Obter primeiro dígito:
#     1 - Multiplicar os 9 primeiros dígitos do CPF por uma contagem
#         regressiva iniciando de 10 e terminando em 2
#     2 - Somar todos os valores das multiplicações do passo 1
#     3 - Obter o resto da divisão entre a soma e 11 do passo 2
#     4 - Subtrair o resultado do passo 3 por 11
#     5 - Se o resultado do passo 4 for maior que nove, o dígito é zero,
#         caso contrário, o dígito é o valor do passo 4

# * Obter segundo dígito:
#     1 - Multiplicar os 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO
#         obtido anteriormente por uma contagem regressiva iniciando de 11
#         e terminando em 2
#     2 - Mesma lógica do passo 2 do primeiro dígito em diante.

# Observações:
#     Tomar cuidado com sequência de caracteres,
#     elas podem gerar CPFs válidos.


# * Obter primeiro dígito:
#Captação do CPF

flag = True

while(flag):
    
    cpf = input("Digite seu CPF: ")
    cpfValid = []
    a= 0

    for i in cpf:
        if(cpf[a] == '0' or cpf[a] == '1' or cpf[a] == '2' or cpf[a] == '3' or cpf[a] == '4' or cpf[a] == '5' or cpf[a] == '6' or cpf[a] == '7' or cpf[a] == '8' or cpf[a] == '9'):
            letra = int(cpf[a])
            cpfValid.append(letra)
            a += 1
        else:
            a += 1


    a=0

    # Multiplicar os 9 primeiros dígitos do CPF por uma contagem regressiva iniciando de 10 e terminando em 2

    numMultiplicado = []
    multiplicador = 10

    for i in range(1, 10):
        mult = cpfValid[a] * multiplicador
        numMultiplicado.append(mult)
        multiplicador -= 1
        a += 1

    a = 0



    #Somar todos os valores das multiplicações do passo 1

    somaCpf = sum(numMultiplicado)

    #Obter o resto da divisão entre a soma e 11 do passo 2

    restCpf = (somaCpf % 11) 

    # Subtrair o resultado do passo 3 por 11

    primeiroDig = 11 - restCpf 

    #Se o resultado do passo 4 for maior que nove, o dígito é zero, caso contrário, o dígito é o valor do passo 4

    if(primeiroDig > 9):
        primeiroDig = 0
    else:
        primeiroDig = primeiroDig



    if(primeiroDig != cpfValid[9]):
        print(cpfValid[9])
        print("Cpf inválido")
        flag = False
    else:
        # * Obter segundo dígito:

        #1 - Multiplicar os 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO obtido anteriormente por uma contagem regressiva iniciando de 11 e terminando em 2

        multiplicador = 11
        mult2 = []
        for i in range(1, 11):
            multNum2 = cpfValid[a] * multiplicador
            mult2.append(multNum2)
            multiplicador -= 1
            a += 1


        # 2 - Somar todos os valores das multiplicações do passo 1

        somaCpf2 = sum(mult2)

        # 3 - Obter o resto da divisão entre a soma e 11 do passo 2

        restCpf2 = (somaCpf2 % 11) 

        # Subtrair o resultado do passo 3 por 11

        segDigito = 11 - restCpf2

        # Se o resultado do passo 4 for maior que nove, o dígito é zero, caso contrário, o dígito é o valor do passo 4

        if(segDigito > 9):
            segDigito = 0
        else:
            segDigito = segDigito
        
        if(segDigito != cpfValid[10]):
            print(f'O cpf {cpfValid} é invalido')
            flag = False
        else:
            print(f"O cpf {cpfValid} é valido")