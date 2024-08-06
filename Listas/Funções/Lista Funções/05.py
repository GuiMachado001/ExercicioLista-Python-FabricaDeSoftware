# Elaborar uma função para retornar o maior de três números recebidos por parâmetro.
lista = []
def maior():
    return f"O maior numero digitado é {max(lista)}"

i = 0
while(i < 3):
    num = int(input("Digite três numeros: "))
    lista.append(num)
    i +=1

verificar = maior()

print(verificar)