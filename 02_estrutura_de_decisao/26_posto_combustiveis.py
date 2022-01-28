"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    a. Álcool:
    b. até 20 litros, desconto de 3% por litro
    c. acima de 20 litros, desconto de 5% por litro
    d. Gasolina:
    e. até 20 litros, desconto de 4% por litro
    f. acima de 20 litros, desconto de 6% por litro
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combus-
    tível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima
    o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina
    é R$ 2,50 o preço do litro do álcool é R$ 1,90.
--------------------------------------------------------------------------------
"""

print("\n* * * * Combustíveis * * * *\n")

tipo_combustivel = input("Digite o tipo de combustível [A - Álcool |  G - Gasolina]: ").upper()
litros = int(input("Litros de combustível: "))

if tipo_combustivel == "A":
    valor_bruto = litros * 1.90
    if litros <= 20:
        desconto = (3/100) * valor_bruto
    else:
        desconto = (5/100) * valor_bruto
    print(f"\nValor final: R${(valor_bruto - desconto):.2f}\n")

elif tipo_combustivel == "G":
    valor_bruto = litros * 2.5
    if litros <= 20:
        desconto = (4/100) * valor_bruto
    else:
        desconto = (6/100) * valor_bruto
    print(f"\nValor final: R${(valor_bruto - desconto):.2f}\n")

else:
    print("\nErro.\n")
