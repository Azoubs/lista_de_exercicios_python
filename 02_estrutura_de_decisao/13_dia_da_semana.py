"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
13. Faça um Programa que leia um número e exiba o dia correspondente da semana.
    (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
    inválido.
--------------------------------------------------------------------------------
"""

print("\n* * * * Dias da Semana * * * *\n")

dia = int(input("Digite um número correspondente a um dia da semana [1-7]: "))

if dia == 1:
    print("\nDomingo!\n")
elif dia == 2:
    print("\nSegunda!\n")
elif dia == 3:
    print("\nTerça!\n")
elif dia == 4:
    print("\nQuarta!\n")
elif dia == 5:
    print("\nQuinta!\n")
elif dia == 6:
    print("\nSexta!\n")
elif dia == 7:
    print("\nSábado!\n")
else:
    print("\nErro!\n")
