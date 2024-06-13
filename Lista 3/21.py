# Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

num1 = int(input("Digite um numero inteir: "))
num2 = int(input("Digite outro numero inteir: "))

i1 = num1
i2 = num2

listaPar = []
listaImpar = []

if(num1 >= num2):
    while(i1 >= i2):
        if(i1 % 2 == 0):
            listaPar.append(i1)
            i1 -= 1
        else:
            listaImpar.append(i1)
else:
    while(i2 >= i1):
        if(i2 % 2 == 0):
            listaPar.append(i2)
            i2 -= 1
        else:
            listaImpar.append(i2)

for i in listaPar: 
    soma = listaPar[i]

for i in listaImpar:
    mult = listaImpar[i]

print(soma)
print(mult)
print(listaImpar)
print(listaPar)