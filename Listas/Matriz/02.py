l = 4
c = 4

i = 0
z = 0
matriz = []
while (i < l):
    listaLinha = []
    y = 0
    x = 0
    while(x<c):
        linha = int(input(f"Linha {z}, coluna: {y}: "))
        listaLinha.append(linha)
        y+=1
        x+=1
    matriz.append(listaLinha)
    z +=1
    i+=1

print(matriz)