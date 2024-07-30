# Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do MS (50 Kg) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. Gravar na variável excesso a
# quantidade de quilos além do limite e na variável multa o valor da multa que o pescador deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = []

def quantPeixes():
    if(sum(pesoPeixe) > 50):
        quantExtra = sum(pesoPeixe) - 50
        valorTaxa = quantExtra * 4

        return f"Peso extra: {quantExtra} \n Valor a pagar: R${valorTaxa}"
    else:
        return "Sem necessidade de pagar taxa extra"


while True:
    peixes = float(input("Digite o peso do peixe em KG ou digite '0' para sair: "))

    if(peixes == 0):
        break
    else:
        pesoPeixe.append(peixes)


x = quantPeixes()

print(x)