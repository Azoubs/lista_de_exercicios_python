"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
    que calcule seu peso ideal, utilizando as seguintes fórmulas:
    - Para homens: (72.7*h) - 58
    - Para mulheres: (62.1*h) - 44.7
--------------------------------------------------------------------------------
"""

print("\n* * * * Peso Ideal v2 * * * *\n")

altura = float(input("Digite a sua altura: "))
peso_ideal_homens = (72.2 * altura) - 58
peso_ideal_mulheres = (62.1 * altura) - 44.7

print("\nPeso ideal para...")
print(f"Homens: {peso_ideal_homens:.1f}")
print(f"Mulheres: {peso_ideal_mulheres:.1f}\n")
