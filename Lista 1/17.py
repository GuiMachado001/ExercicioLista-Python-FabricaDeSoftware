# 17. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:
# R = G ∗ π/180, sendo G o angulo em graus é R em radianos e π = 3.14.


angGraus = float(input("Digite o valor do angulo em graus: "))

angRadiano = angGraus * 3.14 / 180 

print("O valor de ",angGraus,"° em radianos é: ",angRadiano)