"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
    em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
    é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
    18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
    tinta a serem compradas e o preço total.
--------------------------------------------------------------------------------
"""
import math

print("\n* * * * Loja de Tintas v1 * * * *")

area = int(input("Digite o tamanho da área em m²: "))
litros_necessarios = math.ceil(area / 3)
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_final = latas_necessarias * 80

print(f"\nVocê vai gastar: {litros_necessarios} litros")
print(f"Serão necessárias: {latas_necessarias} latas")
print(f"Preço final: R${preco_final:.2f}\n")
