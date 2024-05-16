# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um 
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
# Consumo (Km/l) Mensagem
# menor que 8 Venda o carro!
# entre 8 e 12 Econômico!
# maior que 14 Super econômico

distKm = float(input("Digite o valor da distância percorrida em Km: "))
litGaso = float(input("Digite a quantidade de litros de gasolina consumidos no percurso: "))

consumo = distKm / litGaso

if(consumo < 8):
    print(f"consumo = {distKm / litGaso} Venda o carro!")
elif(8 <= consumo <= 12):
    print(f"consumo = {distKm / litGaso} Econômico!")
elif(consumo >= 14):
    print(f"consumo = {distKm / litGaso} Super Econômico")