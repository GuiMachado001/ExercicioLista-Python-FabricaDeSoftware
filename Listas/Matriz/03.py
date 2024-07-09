matriz = [[1,2,3,],
          [4,5,6],
          [7,8,9]
         ]

novaMatriz = []


i = 0
z = 0
while(i < len(matriz)):
    linha = []
    coluna = 0
    y=0
    while(y < len(matriz[i])):
        valor = matriz[z][coluna] * 5
        linha.append(valor)
        coluna+=1
        y+=1
    novaMatriz.append(linha)
    i+=1
    z+=1

i = 0
x=0
print("Matriz antiga")
while (x < len(matriz)):
    print(matriz[x])
    x+=1

x = 0
print("Nova Matriz")
while (x < len(novaMatriz)):
    print(novaMatriz[x])
    x+=1
