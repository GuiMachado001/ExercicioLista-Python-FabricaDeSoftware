# def hello():
#     print("Hello World")

# hello()

#-----------------------------------------------------------------

# def hello(nome:str, sobrenome:str, idade:int):
#     print(f"Hello {nome} {sobrenome}, sua idade é de {idade} anos")

# hello("Guilherme", "Machado", 22)

#-----------------------------------------------------------------

def soma (x, y):
    res = x + y
    print(f"Resultado: {res}")

def somar(x, y):
    res = x+y
    return res

def verificaIdade(idade):
    if(idade <= 0):
        return "Idade Inválida"
    elif(idade > 0 and idade < 99):
        return True
    else:
        return False

soma(10,12)
x = somar(22,22)
print(x)
print(somar(25,25))

if (somar(50,51) > 100):
    print("Soma maior que 100")



print(verificaIdade(22))