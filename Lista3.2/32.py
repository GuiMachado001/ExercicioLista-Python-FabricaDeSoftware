# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório 
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que 
# o usuário digitou, um por linha.

i = 0
lista = []
while(i < 5):
    num = int(input("Digite um numero: "))
    lista.append(num)
    i+=1

print(f"A soma dos valores digitados é: {sum(lista)}")

print("Os numeros digitados foram: ")

i=0
while(i < len(lista)):
    print(lista[i])
    i += 1