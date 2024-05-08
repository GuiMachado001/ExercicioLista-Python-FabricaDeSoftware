# 23. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de
# conversão é: L = K/0,45 , sendo K a massa em quilogramas e L a massa em libras


massaQuil = float(input("Digite o valor da massa em quilogramas: "))

massaLibra = massaQuil / 0.45

print("O valor de ",massaQuil,"Kg em Libras: ",massaLibra,"L")