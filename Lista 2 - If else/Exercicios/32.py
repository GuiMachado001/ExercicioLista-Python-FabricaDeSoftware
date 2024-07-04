# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes 
# categorias:
# Categoria Idade
# Infantil 5 a 12
# Juvenil 12 a 17
# Sênior maiores de 18 anos


idade = int(input("Digite a idade do nadador: "))

if( 5 <= idade <= 12):
    print("Categoria: Infantil")
elif(12 < idade <= 17):
    print("Categoria: Juvenil")
elif(idade >= 18):
    print("Categoria: Sênior")