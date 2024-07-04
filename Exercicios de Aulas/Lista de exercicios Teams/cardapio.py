# Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante 
# para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
# Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai escolher o prato 
# desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário,
# “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar
# o valor final (valor do prato + 10%), caso contrário, mostrar o valor final 
# (somente o valor do prato). 

cardapioLista = [
    {'Bife Acebolado': 15.00},
    {'X-burguer': 17.00, },
    {'salada': 10.00},
    {'pizza': 22.00},
    {'feijoada': 25.00},
    {'Lasanha': 22.90}
]

codigo = 200 

for item in cardapioLista:
    nome = list(item.keys())[0]
    valor = item[nome]
    print(f"codigo: {codigo} Nome: {nome}, Valor: R$ {valor:.2f}")
    codigo += 1


sep = ("_____________________________________")

finalizar = True
fecharPedido = True
pedidoAtual = []


while(finalizar):
    
    cod = int(input("Digite o codigo para adicionar o produto ou '0' para finalizar o pedido: "))

    if(cod == 0):
        finalizar = False

    else:
        print(sep)
        match cod:
            case 200:
                print(f'{list(cardapioLista[0].keys())[0]} R$ {list(cardapioLista[0].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[0].values())[0])

                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)

            case 201: 
                print(f'{list(cardapioLista[1].keys())[0]} R$ {list(cardapioLista[1].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[1].values())[0])
                
                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)

            case 202:
                print(f'{list(cardapioLista[2].keys())[0]} R$ {list(cardapioLista[2].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[2].values())[0])
                
                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)

            case 203:
                print(f'{list(cardapioLista[3].keys())[0]} R$ {list(cardapioLista[3].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[3].values())[0])

                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)               
    
            case 204:
                print(f'{list(cardapioLista[4].keys())[0]} R$ {list(cardapioLista[4].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[4].values())[0])

                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)

            case 205:
                print(f'{list(cardapioLista[5].keys())[0]} R$ {list(cardapioLista[5].values())[0]}')
                quant = int(input("Digite a Quantidade do produto: "))
                pedidoAtual.append(quant*list(cardapioLista[5].values())[0])

                TotalSemTaxa = sum(pedidoAtual)
                print(f"Valor Total: R${TotalSemTaxa}")
                
                print(sep)
                
            

        

opcao = True

while(opcao):

    print(sep)
    taxaGarcom = int(input(f"Aceita pagar a gorjeta do garçom referente a 10% sobre o valor dos pratos? \n1 - Sim \n2 - Não \n"))
    print(sep)

    if(taxaGarcom == 2):
        TotalSemTaxa = sum(pedidoAtual)
        print(f"O valor Total do pedido Sem a taxa do garçom ficou em: R${TotalSemTaxa:.2f}")
        print(sep)
        opcao = False

    elif(taxaGarcom == 1):
        TotalComTaxa = sum(pedidoAtual) * 1.10
        print(f"O valor Total do pedido com a taxa do garçom ficou em: R${TotalComTaxa:.2f}")
        print(sep)
        opcao = False
    else:
        print("Opção inválida, favor digitar uma opção válida")
        print(sep)
