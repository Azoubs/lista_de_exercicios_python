"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
    Dica: utilize uma função de arredondamento.
--------------------------------------------------------------------------------
"""

print("\n* * * * Inteiro ou Decimal * * * *\n")

numero = float(input("Digite um número: "))

if numero == round(numero):
    print("\nNúmero inteiro!\n")
else:
    print("\nNúmero decimal!\n")
