"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
    em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
    é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
    18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
    preços em 3 situações:
    -> comprar apenas latas de 18 litros;
    -> comprar apenas galões de 3,6 litros;
    -> misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.
--------------------------------------------------------------------------------
"""
import math

print("\n* * * * Loja de Tintas v2 * * * *\n")

area = int(input("Digite a área a ser pintada: "))

# Calcula a quantidade de litros necessários para pintar toda a área
# Adiciona 10% de folga
litros_necessarios = math.ceil((area / 6) + ((10/100) * math.ceil(area / 6)))

# Apenas latas de 18 litros
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_latas = latas_necessarias * 80

# Apenas galões de 3.6 litros
galoes_necessarios = math.ceil(litros_necessarios / 3.6)
preco_galoes = galoes_necessarios * 25

# Mistura
latas_mistura = math.floor(litros_necessarios / 18)
preco_latas_mistura = latas_mistura * 80
sobra_das_latas = litros_necessarios - (latas_mistura * 18)
galoes_mistura = math.ceil(sobra_das_latas / 3.6)
preco_galoes_mistura = galoes_mistura * 25
preco_final_mistura = preco_latas_mistura + preco_galoes_mistura

# Exibe resultados
print(f"\n* * * * RESULTADO * * * *\n")

print(f"""
----------------------------------------
APENAS LATAS (18L)
Latas necessárias: {latas_necessarias}
Valor total: R${preco_latas:.2f}
----------------------------------------
APENAS GALÕES (3.6L)
Galões necessários: {galoes_necessarios}
Valor total: R${preco_galoes:.2f}
----------------------------------------
MISTURA
Latas necessárias: {latas_mistura}
Galões necessários: {galoes_mistura}
Preços - R$ {preco_latas_mistura:.2f} (latas) e R$ {preco_galoes_mistura:.2f} (galões)
Preço final: R${preco_final_mistura:.2f}
----------------------------------------

""")
