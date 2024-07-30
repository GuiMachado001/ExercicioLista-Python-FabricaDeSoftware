# Crie uma função que imprima a quantidade de dígitos de um determinado número inteiro informado.

def quantDigt(digito):
    valor = len(digito)
    return valor

numero = input("Digite um valor: ")

valor = quantDigt(numero)
print(f"A quanidade de digitos no numero {numero} é de: {valor}")