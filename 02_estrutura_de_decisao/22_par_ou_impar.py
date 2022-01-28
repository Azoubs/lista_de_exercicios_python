"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
    Dica: utilize o operador módulo (resto da divisão).
--------------------------------------------------------------------------------
"""

print("\n* * * * Par ou Ímpar * * * *")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("\nNúmero par!\n")
else:
    print("\nNúmero ímpar!\n")
