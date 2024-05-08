# 44. O restaurante a kilo Bem-Bão cobra R$57,00 por cada quilo de refeição. Escreva um algoritmo
# que leia o peso do prato montado pelo cliente (em gramas) e imprima o valor a pagar. Assuma
# que a balança já desconte o peso do prato.


refeicQuilos = float(input("Qual o peso do prato do cliente em Kg: "))

refeicGramas = refeicQuilos * 1000

valorRefei = 0.057 * refeicGramas

print(f"O peso em gramas é: {refeicGramas}, o valor a pagar é R${valorRefei}")