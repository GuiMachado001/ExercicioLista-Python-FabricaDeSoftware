# 27. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares. A fórmula
# de conversão é: H = M ∗0,0001, sendo M a área em metros quadrados é H a área em hectares.


areaM = float(input("Digite o valor da area em metros quadrados: "))

areaH = areaM * 0.0001

print("O valor de ",areaM,"metros quadrados em hectares: ",areaH,"hectares")