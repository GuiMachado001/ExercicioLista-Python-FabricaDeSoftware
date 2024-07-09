lista = [1,2,3,4,5,6,7,8,9]

matriz = []


i = 0
x = 0
y = 3
p = 0
while(i < 3):
    linha = []
    while(x < y):
        valor = lista[p]
        linha.append(valor)
        x+=1
        p +=1
    matriz.append(linha)
    y+=3
    i+=1
print(matriz)