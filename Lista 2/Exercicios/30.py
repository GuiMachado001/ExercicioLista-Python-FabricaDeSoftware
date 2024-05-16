# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma 
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa 
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado 
# não for válido, mostrar uma mensagem de erro.

estado = int(input("Digite o seu estado \n 1- MG \n 2- SP \n 3- RJ \n 4- MS \n"))
valorProd = float(input("Digite o valor do produto: R$"))

if(estado == 1):
    print(f"A taxa para o produto de R${valorProd} para o estado de Minas Gerais é de: R${valorProd*0.07} \nTotalizando o valor do produto em R${valorProd+(valorProd*0.07)}")
elif(estado == 2):
    print(f"A taxa para o produto de R${valorProd} para o estado de São Paulo é de: R${valorProd*0.12} \nTotalizando o valor do produto em R${valorProd+(valorProd*0.12)}")
elif(estado == 3):
    print(f"A taxa para o produto de R${valorProd} para o estado de Rio de Janeiro é de: R${valorProd*0.15} \nTotalizando o valor do produto em R${valorProd+(valorProd*0.15)}")
elif(estado == 4):
    print(f"A taxa para o produto de R${valorProd} para o estado de Mato Grosso do Sul é de: R${valorProd*0.08} \nTotalizando o valor do produto em R${valorProd+(valorProd*0.08)}")
else:
    print("Opção inválida")