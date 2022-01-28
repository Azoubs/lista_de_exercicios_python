"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
06. Faça um Programa que leia três números e mostre o maior deles.
--------------------------------------------------------------------------------
"""

print("\n* * * * Maior de Três Números * * * *\n")

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"\n{num_1} é o maior.\n")
elif num_2 > num_1 and num_2 > num_3:
    print(f"\n{num_2} é o maior.\n")
elif num_3 > num_1 and num_3 > num_2:
    print(f"\n{num_3} é o maior.\n")
