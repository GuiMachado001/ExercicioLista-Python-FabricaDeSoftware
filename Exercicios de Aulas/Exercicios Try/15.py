# Faça um algoritmo que receba um número e apresente a tabuada do mesmo ao final;

try:
        
    num = int(input("digite um numero: "))
    contador = 0
    
    if(num < 0):
        raise ValueError("não são permitidos numeros negativos")

    while(contador <= 10):
        print(f"{num} x {contador} = {contador * num}")
        contador += 1

except ValueError as e:
    print(f"Erro de execução: {e}")