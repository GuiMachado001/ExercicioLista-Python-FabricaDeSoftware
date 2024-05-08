# 42. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a
# escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.


alturaDeg = float(input("Digite o valor da altura do degrau: "))
alturaDesej = float(input("Digite o valor da altura que deseja alcançar: "))

quantDeg = alturaDesej / alturaDeg

print("A quantidade de degraus que deverá ser consruida é de: ",quantDeg,"degraus")