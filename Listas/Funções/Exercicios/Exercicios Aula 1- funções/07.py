# Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago conforme o número de horas trabalhadas. Considere a carga
# horária de 40h por semana como salário base, caso ultrapasse o limite de 40h, o funcionário deve receber 50% a mais por hora excedente.

def  salarioPagar(salario, horasTrabalhadas):
    if(horasTrabalhadas <= 40):
        salarioTotal = salario * salario
    elif(horasTrabalhadas >= 40):
        salarioTotal = (salario * salario ) * 0.5
    return salarioTotal

salarioPorH = float(input("Digite o valor de salario por hora: "))
horasTrab = float(input("Digite a quantidade de Horas trabalhadas: "))

salario = salarioPagar(salarioPorH, horasTrab)

print(f"O Valor a pagar de salario é de {salario} Reais")