# dicione na função calcularTempo() do sistema para estacionamento o valor dos impostos pago pelo cliente. Considereo PIS: 0,33% , COFINS: 0,20% e ICMS: 17% no valor e imprima o
# recibo do cliente de acordo com a saída abaixo:

def calcularEstacionamento(minutos):
    horas = minutos / 60
    if(minutos <= 15):
        return "Estacionamento não será cobrado"
    elif(horas <= 1):
        valorPorHora = 9
        pis = valorPorHora * 0.33
        cofins = valorPorHora * 0.20
        icms = valorPorHora * (17 / 100)
        total = valorPorHora + pis + cofins + icms
        return f"Valor a pagar: \nPis{pis} \n{cofins} \n{icms} \n{total}"
    elif(horas > 1):
        valorAdicional = (horas - 1) * 1.50
        valorTotal = valorAdicional + 9
        
        pis = valorTotal * 0.33
        cofins = valorTotal * 0.20
        icms = valorTotal * (17 / 100)
        total = valorTotal + pis + cofins + icms
        return f"Valor a pagar: \nPis{pis} \n{cofins} \n{icms} \n{total}"

minutos = float(input("Digite em minutos o tempo do estacionamento: "))

print(calcularEstacionamento(minutos))