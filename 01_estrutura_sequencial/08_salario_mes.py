"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
08. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
    trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
--------------------------------------------------------------------------------
"""

print("\n* * * * Salário * * * *\n")

valor_por_hora = float(input("Digite quanto ganha por hora trabalhada: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
salario_final = valor_por_hora * horas_trabalhadas

print(f"\nSalário final: R${salario_final:.2f}\n")
