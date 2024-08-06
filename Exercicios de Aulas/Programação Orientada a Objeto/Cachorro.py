class Cachorro:
    def __init__(self, nome, idade, peso, cor):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.cor = cor
    ## métodos
    def latir(self):
        print(f"{self.nome} Au Au")

    def comer(self):
        print(f"{self.nome} comeu")
    
    def dormir(self, quantidade):
        print(f"{self.nome} Dormiu {quantidade} horas")

dog1 = Cachorro("Bilu", 2, 5, "Branco")
print(dog1.nome)
print(dog1.cor)

print()
dog2 = Cachorro("Belinha",10, 2.5, "Caramelo")
print(dog2.nome)
print(dog2.cor)

print()

dog2.latir()
dog1.comer()
dog1.dormir(2)