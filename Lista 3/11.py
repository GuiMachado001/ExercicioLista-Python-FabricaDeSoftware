# Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 
# primeiros números pares.

i = 0
num = 0
lista = []
while(i < 51):
    if(num % 2 == 0):
        print(f"{num}")
        lista.append(num)
        num += 1
        i += 1
    else:
        num += 1
        
print(sum(lista))
        