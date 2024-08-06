# Crie uma função que receba como argumento uma lista, com
# valores de qualquer tipo. A função deve imprimir todos os
# elementos da lista numerando-os. Exemplo:
# 1, Pera
# 2, Uva
# 3, Maça
# 4, Salada mista


frutas = ['Pera', 'Uva', 'Maça', 'Salada Mista']

def listar(lista):
    i = 0
    while(i < len(lista)):
        print(f"{i+1}, {lista[i]}")
        i +=1

listar(frutas)