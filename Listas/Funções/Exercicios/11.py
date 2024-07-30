# Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento. Ela tem uma quantia X para dar de entrada, uma taxa de juros é definida pelo banco e a
# pessoa pode escolher o número de parcelas que deseja financiar. Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos. O programa 
# deve solicitar ao usuário o valor do veiculo, o valor da entrada, a taxa de juros e a quantidade de parcelas. Além disso, o programa deve exibir o valor total pago, a quantia 
# dos juros pagos e o valor de cada parcela. O programa deve apresentar as informações de forma clara e objetiva, facilitando a compreensão por parte do usuário.

def financiamento(valorVeiculo, valorEntrada, taxaJuros, quantParcelas):
    taxaJuros = taxaJuros /100
    valorPagar = valorVeiculo - valorEntrada
    valorParcelas = valorPagar / quantParcelas
    i = 0
    while(i < quantParcelas):
        totalParcelas = valorParcelas * taxaJuros
        i +=1
        return totalParcelas
valorVeiculo = float(input("Digite o valor do veículo: "))
valorEntrada = float(input("Digite o valor da entrada: "))
taxaJuros = float(input("Digite a '%' de juros: "))
quantParcelas = int(input("Digite a quantidade de parcelas: "))

print(financiamento(valorVeiculo, valorEntrada, taxaJuros, quantParcelas))