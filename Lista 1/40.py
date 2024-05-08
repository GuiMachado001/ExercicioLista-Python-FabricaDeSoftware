# 40. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que
# esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de
# imposto sobre o salário-base.


salarioFunc = float(input("Qual o valor do salario do funcionario? "))

gratificacao = salarioFunc * 0.05
salarioLiqu = gratificacao + (salarioFunc * 0.93)

print(f"O valor que deve pagar para o funcionario com o adicional de 5% de e o imposto de 7% é igual R%",salarioLiqu)