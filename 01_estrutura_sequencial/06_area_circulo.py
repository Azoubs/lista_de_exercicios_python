"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
06. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
--------------------------------------------------------------------------------
"""
import math

print("\n* * * * Área do Círculo * * * *\n")

raio = float(input("Digite o raio: "))
area = math.pi * (raio * raio)

print(f"\nA área do círculo é: {area:.2f}\n")
