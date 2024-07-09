matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
         ]

novaMatriz = []

x = 0
y= 0
z = 0
for i in matriz:
    linha = []
    coluna = 0
    y = 0
    for x in matriz[0]:
        valor = matriz[z][coluna] * 5
        linha.append(valor)
        y+=1
        coluna += 1
    novaMatriz.append(linha)
    z+=1

print(novaMatriz)

