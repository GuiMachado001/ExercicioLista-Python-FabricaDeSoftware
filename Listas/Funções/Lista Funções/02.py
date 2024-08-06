# Faça uma função que receba a data atual (dia, mês e ano) e exiba-a na tela no formato
# textual por extenso. Exemplo: Data: 01/01/2000, Imprimir: 1 de janeiro de 2000.

listaMes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

def dataAtual(dia, mes, ano):
    mes = mes - 1
    mesEscrito = listaMes[mes]
    print(f"{dia}/{mesEscrito}/{ano}")


data = input("Digite a data atual (formato 01/01/2000): ")

dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)

dataAtual(dia,mes,ano)