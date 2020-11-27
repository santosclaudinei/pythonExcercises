# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

######################################################################################################
def calcula_Tudo(salario):
    desc_inss = salario * (8 / 100)
    desc_irpf = salario * (11 / 100)
    desc_sindicato = salario * (5 / 100)
    salario_liquido = salario - desc_irpf -desc_inss - desc_sindicato
    print(f'O salario bruto com base nos calculos do sistema de RH é R$ {salario}')
    print(f'O desconto referente à taxa recolhida pelo INSS com base nos calculos do sistema de RH é R$ {desc_inss}')
    print(f'O desconto referente à taxa recolhida pelo SINDICATO calculos do sistema de RH é R$ {desc_sindicato}')
    print(f'O desconto referente à taxa retida na folha para Imposto de Renda com base nos calculos do sistema de RH'
          f' é R$ {desc_irpf}')
    print(f'O seu salario final com todos os descontos é de R$ {salario_liquido}')


valor_hora_trabalhada = float(input('Informe quanto você ganha por hora: '))
num_horas_trabalhadas = int(input('Informe o numero de horas que trabalhou nesse mês: '))
salario_bruto = valor_hora_trabalhada * num_horas_trabalhadas
calcula_Tudo(salario_bruto)

