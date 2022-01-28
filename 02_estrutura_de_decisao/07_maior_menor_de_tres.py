"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
07. Faça um Programa que leia três números e mostre o maior e o menor deles.
--------------------------------------------------------------------------------
"""

print("\n* * * * Maior & Menor de Três Números * * * *\n")

maior, menor = None, None

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))

# Encontra o maior
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
elif num_2 > num_1 and num_2 > num_3:
    maior = num_2
elif num_3 > num_1 and num_3 > num_2:
    maior = num_3
else:
    maior = "Existem números iguais"

# Encontra o menor
if num_1 < num_2 and num_1 < num_3:
    menor = num_1
elif num_2 < num_1 and num_2 < num_3:
    menor = num_2
elif num_3 < num_1 and num_3 < num_2:
    menor = num_3
else:
    menor = "Existem números iguais"

# Resultados
print(f"\nMenor número: {menor}")
print(f"Maior número: {maior}\n")
