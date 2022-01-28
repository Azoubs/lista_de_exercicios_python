"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre
    em graus Fahrenheit.
--------------------------------------------------------------------------------
"""

print("\n* * * * Celsius para Fahrenheit * * * *\n")

cel = float(input("Digite a temperatura em °C: "))
fah = (cel * 9 / 5) + 32

print(f"\n{cel:.1f}°C = {fah:.1f}°F\n")
