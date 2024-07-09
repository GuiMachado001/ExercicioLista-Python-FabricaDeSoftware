# Escreva um programa que calcule e escreva o valor de S

soma = 0 
denominador = 1
numerador = 1

while(denominador<=50):
    soma += numerador/denominador
    numerador += 2
    denominador +=1

print(soma)