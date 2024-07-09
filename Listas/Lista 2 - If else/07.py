# Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor 
# de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser 
# vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um 
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

valorProduto = float(input("Digite o valor do Produto: R$"))

if(valorProduto < 50.00):
    valorFinal = valorProduto * 1.45

    print(f"O valor do produto fica em {valorFinal}")
else:
    valorFinal = valorProduto * 1.30
    print(f"O valor do produto fica em {valorFinal}")
