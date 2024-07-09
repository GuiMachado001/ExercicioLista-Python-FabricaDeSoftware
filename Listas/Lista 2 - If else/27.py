# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se 
# forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
# • Chama-se equilátero o triângulo que tem três lados iguais.
# • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

#Classificar um triangulo de acordo com seus lado

ladoA = float(input("Digite o valor do lado 1: "))
ladoB = float(input("Digite o valor do lado 2: "))
ladoC = float(input("Digite o valor do lado 3: "))


if(ladoA == ladoB and ladoC < ladoA):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(ladoB == ladoC and ladoA < ladoB):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(ladoC == ladoA and ladoB < ladoA):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(ladoA == ladoB and ladoC):
    print("É um triangulo Equilatero (Todos os lados são iguais)")
else:
    print("Triangulo Escaleno (Todos os lados são diferentes)")