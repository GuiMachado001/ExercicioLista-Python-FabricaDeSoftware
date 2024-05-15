# Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7∗ h)−58
# • Mulheres: (62,1∗ h)−44,7

sexo = input("Digite F para Feminino e M para Masculino: ")
altura = float(input("Digite a sua altura: "))

if(sexo == 'M' or sexo == 'm'):
    print(f"O peso ideal para a sua altura é de {(72.7 * altura)-58}")
else:
    print(f"O peso ideal para a sua altura é de {(62.1 * altura)-44.7}")
