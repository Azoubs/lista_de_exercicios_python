"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
08. Faça um programa que pergunte o preço de três produtos e informe qual produto
    você deve comprar, sabendo que a decisão é sempre pelo mais barato.
--------------------------------------------------------------------------------
"""

print("\n* * * * Produtos * * * *\n")

prod_1 = float(input("Digite o valor do primeiro produto: "))
prod_2 = float(input("Digite o valor do segundo produto: "))
prod_3 = float(input("Digite o valor do terceiro produto: "))

if prod_1 < prod_2 and prod_1 < prod_3:
    print("\nVocê deve comprar o primeiro produto.\n")
elif prod_2 < prod_1 and prod_2 < prod_3:
    print("\nVocê deve comprar o segundo produto.\n")
elif prod_3 < prod_1 and prod_3 < prod_2:
    print("\nVocê deve comprar o terceiro produto.\n")
