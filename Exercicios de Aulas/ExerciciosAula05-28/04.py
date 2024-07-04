# Faça um algoritmo que receba o número de avaliações do estudante que será (utilizado como contador),
# após receba as notas e apresente a média do estudante.

i = int(input("Digite a quantidade de avaliações que o estudante recebeu: "))
avaliacao = 1
notas = []
valorMedia = i

while (i > 0):
    nota = float(input(f"Digite a nota da avaliação {avaliacao}: "))
    notas.append(nota)
    i -= 1
    avaliacao += 1

media = sum(notas) / valorMedia

print(f"A média do aluno é {media}")