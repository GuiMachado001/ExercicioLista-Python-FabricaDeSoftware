# Faça um algoritmo que mostre um Menu com opções de um cardápio de restaurante 
# para uma pessoa (Coloque no mínimo 5 opções e máximo 10 opções de cardápio. 
# Ex: Bife acebolado R$15,00; Lasanha R$25,00). A pessoa vai escolher o prato 
# desejado e após escolher o prato, o algoritmo deverá fazer a seguinte pergunta ao usuário,
# “Aceita pagar a gorjeta do garçom 10% sobre o valor do prato”. Se o usuário aceitar, mostrar
# o valor final (valor do prato + 10%), caso contrário, mostrar o valor final 
# (somente o valor do prato). 
import match  

cardapioLista = [
    {'Bife Acebolado': 15.00},
    {'X-burguer': 17.00, },
    {'salada': 10.00},
    {'pizza': 22.00},
    {'feijoada': 25.00},
    {'Lasanha': 22.90}
]


cod = 200

for item in cardapioLista:
    nome = list(item.keys())[0]
    valor = item[nome]
    print(f"codigo: {cod} Nome: {nome}, Valor: R$ {valor:.2f}")
    cod += 1

match cod:
    case 200:
        print('Bi')