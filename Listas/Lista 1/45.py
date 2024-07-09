# 45. Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
# vendida respectivamente por 35, 45 e 55 reais. Construa um algoritmo em que o usuário forneça
# a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
# informe quanto será o valor arrecadado.



valorCamisaP = 35
valorCamisaM = 45
valorCamisaG = 55

quantCamisaP = int(input("Digite a quantidade de camisas tamanho P: "))
quantCamisaM = int(input("Digite a quantidade de camisas tamanho M: "))
quantCamisaG = int(input("Digite a quantidade de camisas tamanho G: "))


totalValorCamisaP = quantCamisaP * valorCamisaP
totalValorCamisaM = quantCamisaM * valorCamisaM
totalValorCamisaG = quantCamisaG * valorCamisaG

valorTotal = totalValorCamisaP + totalValorCamisaM + totalValorCamisaG


print(f"O valor da total a se pagar é: R${valorTotal}, sendo:\n Camisas P: R${totalValorCamisaP}\n Camisas M: R${totalValorCamisaM} \n Camisas G: R${totalValorCamisaG}")