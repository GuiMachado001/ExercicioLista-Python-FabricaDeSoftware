# 18. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:
# G = R ∗180/π, sendo G o angulo em graus é R em radianos e π = 3.14.


angRadiano = float(input("Digite o valor do angulo em Radianos: "))

angGraus = angRadiano * 180 / 3.14  

print("O valor de ",angRadiano," em graus é: ",angGraus,"°")