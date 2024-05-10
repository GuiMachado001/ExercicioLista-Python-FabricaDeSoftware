#Classificar um triangulo de acordo com seus lado

lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if(lado1 == lado2 and lado3 < lado1):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(lado2 == lado3 and lado1 < lado2):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(lado3 == lado1 and lado2 < lado1):
    print("É um triangulo isóceles (Dois lados iguais e um menor)")
elif(lado1 == lado2 and lado3):
    print("É um triangulo Equilatero (Todos os lados são iguais)")
else:
    print("Triangulo Escaleno (Todos os lados são diferentes)")