def fahrenheit(f):
    return (f-32) * 5/9

while(True):
    tempF = float(input("insira a temperatura em fahrenheit: "))
    
    try:
        celsius = fahrenheit(tempF)
        print(f"{tempF}°F equivale a {celsius:.2f}°c")
        break
    except ValueError:
        print("Esse valor é inválido para a temperatura. Por favor entre com um numero")