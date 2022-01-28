"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
09. Faça um Programa que leia três números e mostre-os em ordem decrescente.
--------------------------------------------------------------------------------
"""

print("\n* * * * Ordem Decrescente * * * *\n")

maior, meio, menor = None, None, None

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

if num_1 > num_2 and num_1 > num_3:
    maior = num_1
    if num_2 > num_3:
        meio = num_2
        menor = num_3
    else:
        meio = num_3
        menor = num_2

elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
    if num_1 > num_3:
        meio = num_1
        menor = num_3
    else:
        meio = num_3
        menor = num_1

elif num_3 > num_2 and num_3 > num_1:
    maior = num_3
    if num_1 > num_2:
        meio = num_1
        menor = num_2
    else:
        meio = num_2
        menor = num_1

print(f"\n{maior} > {meio} > {menor}\n")
