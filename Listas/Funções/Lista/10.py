# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a
# letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá
# calcular a média ponderada, com pesos 5, 3 e 2.

def calculoMedia(n1,n2,n3,opcao):
    if(opcao == 'A' or opcao == 'a'):
        media = (n1 + n2 + n3) / 5
        return f"A média aritimética é de {media}"
    else:
        media = ((5*n1) + (3*n2) + (2*n3)) / (5+3+2)
        return f"A média ponderada é de {media}"


n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))
opcao = input("Digite 'A' para calcular a média aritimética e 'P' para calcular a média ponderada: ")

media = calculoMedia(n1,n2,n3,opcao)

print(media)