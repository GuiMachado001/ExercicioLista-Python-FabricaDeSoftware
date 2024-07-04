# Chico tem 1.70 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.20 metros e cresce 3 
# centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão 
# necessários para que Zé seja maior que Chico.


chico = 170
ze = 120

ano = 0
while(ze <= chico):
    chico += 2
    ze += 3
    ano += 1

chico /= 100
ze /= 100
print(f"Em {ano} anos ze tera {ze} metros")
print(f"Em {ano} anos chico tera {ze} metros")
print(f"Levará {ano} anos para ")
