# Crie uma função que receba como argumento a
# potência elétrica de determinado aparelho e o tempo
# ligado e retorne o consumo em KWh em seguida chame
# outra função para calcular a conta de energia, levando
# em consideração o consumo e o valor do KWh como
# argumentos.
def contaEnergia(consumo):
    valor = consumo * 0.80
    return valor

def CalcConsumo(potencia, tempo):
    consumo = (potencia * tempo ) / 1000
    return contaEnergia(consumo)


potencia = float(input("Digite a potência elétrica do aparelho: "))
tempo = float(input("Digite o tempo que o aparelho esteve ligado em horas: "))

total = CalcConsumo(potencia, tempo)
print(total)