"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
    e lhe contraram para desenvolver o programa que calculará os reajustes. Faça
    um programa que recebe o salário de um colaborador e o reajuste segundo o
    seguinte critério, baseado no salário atual:
    -> salários até R$ 280,00 (incluindo) : aumento de 20%
    -> salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    -> salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    -> salários de R$ 1500,00 em diante : aumento de 5%

    Após o aumento ser reali-zado, informe na tela:
    -> o salário antes do reajuste;
    -> o percentual de aumento aplicado;
    -> o valor do aumento;
    -> o novo salário, após o aumento.
--------------------------------------------------------------------------------
"""

print("\n* * * * Calculadora de Aumento * * * *\n")

aumento_perc, valor_aumento, novo_salario = 0, 0, 0

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    aumento_perc = 20
elif salario > 280 and salario <= 700:
    aumento_perc = 15
elif salario > 700 and salario <= 1500:
    aumento_perc = 10
elif salario > 1500:
    aumento_perc = 5

valor_aumento = (aumento_perc/100) * salario
novo_salario = salario + valor_aumento

print(f"""
-----------------------------------------------
* * RESULTADOS * *

Salário inicial: R$ {salario:.2f}
Porcentagem do aumento: {aumento_perc}%
Valor do aumento: R$ {valor_aumento:.2f}
Novo salário: R$ {novo_salario:.2f}
-----------------------------------------------
""")
