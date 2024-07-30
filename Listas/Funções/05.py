# Escreva um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. Por fim deve retornar o novo
# valor para o usuário considerando o percentual do imposto.


def taxaimposto(valorTaxa, custo):
    valorImposto = valorTaxa / 100

    resultadoTaxa = custo * valorImposto

    valorTotal = custo + resultadoTaxa
    return valorTotal

valorTaxa = int(input("Digite o valor da taxa de imposto(em porcentagem): "))
custo = int(input("Digite o valor do produto: "))

valorTotal = taxaimposto(valorTaxa, custo)

print(f"O valor total do produto é de: {valorTotal}")