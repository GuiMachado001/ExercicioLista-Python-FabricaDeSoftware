# 21. Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. A fórmula de
# conversão é: L = 1000∗ M, sendo L o volume em litros e M o volume em metros cúbicos.


volMc = float(input("Digite o valor do volume em metros cubicos: "))

volLit = 1000 * volMc

print("O valor de ",volMc," em volume litros é: ",volLit,"L")