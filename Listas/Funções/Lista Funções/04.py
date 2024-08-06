# Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos
# e segundos, e os converta em segundos.

def horario(horas, minutos, segundos):
    horasEmMinutos = horas * 60
    minutosEmSegundos = (minutos + horasEmMinutos) * 60
    totalSeguntos = minutosEmSegundos + segundos
    return f"{totalSeguntos}segundos"


time = input("Digite as horas, minutos e segundos (formato 00:00:00): ")

horas, minutos, segundos = time.split(":")

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

converter = horario(horas, minutos, segundos)
print(converter)