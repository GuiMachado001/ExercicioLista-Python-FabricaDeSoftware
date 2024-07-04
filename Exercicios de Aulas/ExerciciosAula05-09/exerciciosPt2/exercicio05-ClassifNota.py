#Classificar um aluno de acordo com sua nota em A,B,C,D ou F

nota = float(input("Por favor digite a nota do aluno: "))

if(nota >= 9):
    print("Aluno classe A")

elif(nota >= 7 or nota == 8):
    print("Aluno classe B")

elif(nota >= 5 or nota == 6):
    print("Aluno classe C")

elif(nota >= 3 or nota == 4):
    print("Aluno classe D")

elif(nota >= 1 or nota ==  2):
    print("Aluno classe E")

elif(nota == 0):
    print("Aluno classe F")