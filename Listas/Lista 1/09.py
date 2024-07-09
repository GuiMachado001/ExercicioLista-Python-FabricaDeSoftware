# 9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula
# de conversão é: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura
# em Celsius.

tempCelsius = float(input("Por favor digite a temperatura em Celsius: "))

fahrenheit = tempCelsius * (9 / 5) + 32

print("o valor de ",tempCelsius,"°c em fahrenheit é igual a: ",fahrenheit)