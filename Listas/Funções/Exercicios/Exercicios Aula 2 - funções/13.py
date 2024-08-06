# Crie uma função que retorne uma lista com valor
# padrão. Para esta função, consideraremos como argumentos
# de entrada a quantidade de elementos e o valor padrão a
# ser atribuído a todos eles. Exemplo de retorno:
# [1,1,1,1,1,1,1,1]
# [“A”,”A”,”A”,”A”]


def criarLista(quant, valor):
    lista = []

    for i in range(quant):
        lista.append(valor)
    return lista

tamanho = int(input("Digite o tamanho da lista: "))
valor = int(input("Digite o valor: "))

res = criarLista(tamanho, valor)
print(res)