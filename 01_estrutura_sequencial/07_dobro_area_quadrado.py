"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 28.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
07. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
    desta área para o usuário.
--------------------------------------------------------------------------------
"""

print("\n* * * * Dobro da Área de um Quadrado * * * *\n")

lado = int(input("Digite o valor do lado: "))
area = lado * lado
dobro_area = area * 2

print(f"\nÁrea do quadrado: {area}\nDobro da área: {dobro_area}\n")
