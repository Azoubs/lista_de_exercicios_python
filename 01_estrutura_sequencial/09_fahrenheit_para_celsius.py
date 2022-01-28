"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
09. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
    mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
--------------------------------------------------------------------------------
"""

print("\n* * * * Fahrenheit para Celsius * * * *\n")

fah = float(input("Digite a temperatura em Fahrenheit: "))
cel = 5 * ((fah - 32) / 9)

print(f"\n{fah:.1f}°F = {cel:.1f}°C\n")
