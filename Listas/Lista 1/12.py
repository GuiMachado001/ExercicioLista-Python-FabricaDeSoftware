# 12. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de
# conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

tempCelsius = float(input("Por favor digite a temperatura em Celsius: "))

kelvin = tempCelsius + 273.15

print("o valor de ",tempCelsius,"°c em kelvin é igual a: ",kelvin)