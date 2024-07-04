while(True):
    try: 
        x = int(input("Digite um numero: "))
        y = int(input("Digite um numero: "))

        if(y == 0):
            raise RuntimeError("Divisão por zero não é permitida.")

        resultado = x / y
        print(f"O resultado é: {resultado}")
    except RuntimeError as e:
        print(f"Erro de Execussão: {e}")
    except ValueError:
        print("Erro: Entrada inválida! por favor, digite um número.")