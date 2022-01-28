"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                              Até 5 Kg           Acima de 5 Kg
        Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
        Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultra-
    passar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva
    um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
    de maças adquiridas e escreva o valor a ser pago pelo cliente.
--------------------------------------------------------------------------------
"""

print("\n* * * * Fruteira * * * *\n")

morango = int(input("Digite o peso (em kg) de morangos: "))
maca = int(input("Digite o peso (em kg) de maçãs: "))

morango_valor_kg, maca_valor_kg = 0, 0
desconto, valor_final = 0, 0

if morango <= 5:
    morango_valor_kg = 2.50
elif morango > 5:
    morango_valor_kg = 2.20

if maca <= 5:
    maca_valor_kg = 1.80
elif maca > 5:
    maca_valor_kg = 1.50

valor_bruto_morango = morango * morango_valor_kg
valor_bruto_maca = maca * maca_valor_kg
valor_somado = valor_bruto_morango + valor_bruto_maca

if (morango + maca) > 8 or valor_somado > 25:
    print("\nDesconto de 10%!")
    desconto = (10/100) * valor_somado
else:
    print("\nSem desconto!")
    desconto = 0

valor_final = valor_somado - desconto
print(f"\nValor final: R$ {valor_final:.2f}\n")
