# 20. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A
# fórmula de conversão é P = C/2,54 , sendo C o comprimento em centímetros e P o comprimento
# em polegadas.


compCent = float(input("Digite o valor do comprimento em centimetros: "))

compPoleg = compCent / 2.54  

print("O valor de ",compCent," em centimetros é: ",compPoleg)