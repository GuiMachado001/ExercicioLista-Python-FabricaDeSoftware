matriz = [[1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          ]

l = int(input("Digite a linha que deseja alterar: "))
c = int(input("Digite a coluna que deseja alterar: "))

matriz[l][c] = 'x'

x = 0
while (x < len(matriz)):
    print(matriz[x])
    x+=1