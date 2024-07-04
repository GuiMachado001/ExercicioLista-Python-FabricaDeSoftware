# Faça um algoritmo que inicialize uma lista de 10 cidades que deseja conhecer e 
# apresente em ordem decrescente (da última para a primeira);

cidades = ["Bonito", "São Paulo", "Rio de Janeiro", "Gramado", "Porto Alegre", "Terenos", "Fortaleza", "Recife","Porto Seguro", "Umuarama"]
cidades.sort(reverse=True)
i = 0 
while(len(cidades) > i):
    print(cidades[i])
    i += 1