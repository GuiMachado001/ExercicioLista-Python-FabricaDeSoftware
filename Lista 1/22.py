# 22. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. A fórmula de
# conversão é: M = L / 1000 , sendo L o volume em litros e M o volume em metros cúbicos


volLit = float(input("Digite o valor do volume em litros: "))

volMc = 1000 / volLit

print("O valor de ",volLit," em metros cubicos é: ",volMc)