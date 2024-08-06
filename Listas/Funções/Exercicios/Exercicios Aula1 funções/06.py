# Um comerciante possui uma loja de artigos de R$ 1,99. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens
# que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços.
# Você foi contratado para desenvolver uma função que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

def tabela():
    produto = 1.99
    i = 1
    while(i <= 50):
        print(produto *i)
        i+=1
tabela()