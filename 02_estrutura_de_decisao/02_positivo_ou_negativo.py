"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
02. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou
    negativo.
--------------------------------------------------------------------------------
"""

print("\n* * * * Positivo ou Negativo * * * *\n")

numero = int(input("Digite um número: "))

if numero >= 0:
    print(f"\n{numero} é positivo!\n")
else:
    print(f"{numero} é negativo!\n")
