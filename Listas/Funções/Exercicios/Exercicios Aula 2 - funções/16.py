# Crie uma função que receba múltiplos
# argumentos não nomeados, considere que a
# função receba números flutuantes como
# argumentos e retorne a média dos
# argumentos.

def media(*args):
    media = sum(args) / len(args)
    return media


valor = input("Digite os numeros para fazer a media (Formato: 2,3,4,5): ")
valorFloat = [float(x) for x in valor.split(",")]

resultado = media(*valorFloat)
print(resultado)
