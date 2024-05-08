# 15. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão
# é: K = 1,61∗ M, sendo K a distância em quilômetros M em milhas


distMilhas = float(input("Digite o valor da distancia em milhas: "))

distancKm = 1,61 * distMilhas 

print("O valor de ",distMilhas,"milhas em Km é: ",distancKm,"Km")