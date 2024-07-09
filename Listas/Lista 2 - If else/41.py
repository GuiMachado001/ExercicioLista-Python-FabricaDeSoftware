# Calcule as raízes da equação de 2o grau.
# Lembrando que:
# Onde
# ∆ = B2−4ac
# E ax2+ bx + c = 0 representa uma equação de 2o grau.
# A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação 
# de segundo grau”.
# i. Se ∆ < 0, não existe real. Imprima a mensagem: Não existe raiz.
# ii. Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única.
# iii. Se ∆ ≥ 0, imprima as duas raízes reais

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

x1 = (-b + (delta**0.5) ) / (2*a)
x2 = (-b - (delta**0.5) ) / (2*a)

print(f"O Valor de delta é: {delta}")
print(f"O Valor de x1 = {x1}")
print(f"O Valor de x2 = {x2}")
