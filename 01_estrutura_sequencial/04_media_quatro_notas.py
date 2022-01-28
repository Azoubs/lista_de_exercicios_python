"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
04. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
--------------------------------------------------------------------------------
"""

print("\n* * * * Média de Quatro Notas * * * *\n")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))
nota_4 = float(input("Digite a quarta nota: "))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"\nMédia final: {media:.1f}\n")
