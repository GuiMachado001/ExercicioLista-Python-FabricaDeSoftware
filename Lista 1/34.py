# 34. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um
# cilindro circular e calculado por meio da seguinte fórmula V = π ∗ raio2 ∗ altura, onde π =
# 3.141592.


altura = float(input("Digite o valor da altura do cilindro: "))
raio = float(input("Digite o valor do raio do cilindro: "))

volume = 3.14 * (raio*raio) * altura

print("O valor do volume do cilindro é: ",volume)