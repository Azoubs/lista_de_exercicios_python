"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
    calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
--------------------------------------------------------------------------------
"""

print("\n* * * * Peso Ideal * * * *\n")

altura = float(input("Digite a altura: "))
peso_ideal = (72.7 * altura) - 58

print(f"\nSeu peso ideal é: {peso_ideal:.1f} kg\n")
