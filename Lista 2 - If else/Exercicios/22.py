# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente 
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

num = int(input("Digite um numero entre 1 e 7: "))

if(num == 1):
    print("Dia da semana equivalente à: Domingo")
elif(num == 2):
    print("Dia da semana equivalente à: Segunda")
elif(num == 3):
    print("Dia da semana equivalente à: Terça")
elif(num == 4):
    print("Dia da semana equivalente à: Quarta")
elif(num == 5):
    print("Dia da semana equivalente à: Quinta")
elif(num == 6):
    print("Dia da semana equivalente à: Sexta")
elif(num == 7):
    print("Dia da semana equivalente à: Sábado")