# 28. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2.
# A fórmula de conversão é: M = H ∗10000, sendo M a área em metros quadrados é H a área em
# hectares


areaH = float(input("Digite o valor da area em hectares: "))

areaM = areaH * 10000

print("O valor de ",areaH,"hectares em metros quadrado: ",areaM,"m2")