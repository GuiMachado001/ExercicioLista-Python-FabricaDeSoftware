# O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, a principal função do sistema é calcularTempo(). Considere o valor mínimo de R$9,00
# por hora e R$ 1,50 por hora adicional. O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. Caso o usuário fique no estacionamento por
# menos de 15 minutos, o tempo utilizado não será cobrado.

def calcularEstacionamento(minutos):
    horas = minutos / 60
    if(minutos <= 15):
        return "Estacionamento não será cobrado"
    elif(horas <= 1):
        return "Valor a pagar R$9,00"
    elif(horas > 1):
        valorAdicional = (horas - 1) * 1.50
        valorTotal = valorAdicional + 9
        return f"Valor total a pagar: R${valorTotal}"

minutos = float(input("Digite em minutos o tempo do estacionamento: "))

print(calcularEstacionamento(minutos))