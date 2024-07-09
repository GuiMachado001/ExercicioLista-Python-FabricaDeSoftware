# 11. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de
# conversão é: C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.


tempKelvin = float(input("Digite o valor da temperatura em graus Kelvin: "))

celsius = tempKelvin - 273.15

print("o valor de ",tempKelvin," em celsius é igual a: ",celsius,"°")