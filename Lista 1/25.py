# 25. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de
# conversão é: M = 0,91∗ J, sendo J o comprimento em jardas e M o comprimento em metros


compJard = float(input("Digite o valor do comprimento em jardas: "))

compMetr = 0.91 * compJard

print("O valor de ",compJard,"jardas em metros: ",compMetr,"m")