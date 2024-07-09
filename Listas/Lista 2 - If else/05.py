# Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: 
# F - Feminino, M – Masculino ou Sexo Inválido.

sexo = input("Digite F para Feminino e M para Masculino: ")

if(sexo == 'F' or sexo == 'f'):
    print("F- Feminino")
elif(sexo == 'M' or sexo == 'm'):
    print("M- Masculino")
else:
    print("Deve-se digitar F ou M")