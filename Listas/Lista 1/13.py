# 13. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros
# por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.


velocKm = float(input("Digite a velocidade em Km/h: "))

metros = velocKm / 3.6

print("O valor de ",velocKm,"Km/h em m/s é: ",metros,"m/s")