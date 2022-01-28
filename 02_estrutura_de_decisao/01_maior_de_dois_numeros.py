"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
01. Faça um Programa que peça dois números e imprima o maior deles.
--------------------------------------------------------------------------------
"""

# Este código assume que serão dados dois valores diferentes

print("\n* * * * Maior de Dois Números * * * *\n")

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

if num_1 > num_2:
    print(f"\n{num_1} > {num_2}\n")
else:
    print(f"\n{num_2} > {num_1}\n")
