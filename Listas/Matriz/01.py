l = 3
c = 3

matriz = []
i = 0
x = 0
while (i < l) :
    linha = []
    j = 0
    while (j < c):
        x = x+1 
        linha.append(x)
        j += 1
    matriz.append(linha)
    i += 1


x = 0

while (x < len(matriz)):
    print(matriz[x])
    x+=1

