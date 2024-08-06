# Crie uma função de um programa de teste para o cálculo do volume de uma esfera. Sendo que o
# raio é passado por parâmetro?
# V = 4/3 ∗ π ∗ R3

def volume(raio):
    volume = ((4 * 3.14) * (raio ** 3)) / 3 
    return volume


raio = input("Digite um numero para o raio: ")

verificar = volume(raio)

print(verificar)