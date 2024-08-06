# Crie uma função que receba a altura e o raio de um cilindro circular e retorne o volume do 
# cilindro. O volume de um cilindro circular e calculado por meio da seguinte fórmula:  
# V = π * raio2 * altura, onde π = 3.141592.

def volume (altura, raio):
    v = 3.14 * ((raio **2) * (altura))
    return f"O valume do cilindro é de {v}cm"

altura = float(input("Digite o valor da altura: "))
raio = float(input("Digite o valor do raio: "))

v = volume(altura, raio)

print(v)