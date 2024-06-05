# Um algoritmo em que usuário escolha uma opção de acordo com o último número da placa do carro 
# e mostre uma mensagem dizendo em que dia da semana não poderá circular. 
# 1 - 2 “Não Circular 2ª Feira” 

# 3 - 4 “Não Circular 3ª Feira” 

# 5 - 6 “Não Circular 4ª Feira” 

# 7 - 8 “Não Circular 5ª Feira” 

# 9 - 0 “Não Circular 6ª Feira” 

numPlaca = int(input("Digite o último número da placa do carro: "))

if(numPlaca == 1 or numPlaca == 2):
    print("Não circular 2ª Feira")
elif(numPlaca == 3 or numPlaca == 4):
    print("Não circular 3ª Feira")
elif(numPlaca == 5 or numPlaca == 6):
    print("Não circular 4ª Feira")
elif(numPlaca == 7 or numPlaca == 8):
    print("Não circular 5ª Feira")
elif(numPlaca == 9 or numPlaca == 0):
    print("Não circular 6ª Feira")
