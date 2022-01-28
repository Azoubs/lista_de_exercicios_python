"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
    usuário a valor do saque e depois informar quantas notas de cada valor serão
    fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
    mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
    com a quantidade de notas existentes na máquina.
    a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas
                  de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas
                  de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
                  notas de 1.
--------------------------------------------------------------------------------
"""

print("\n* * * * Caixa Eletrônico * * * *\n")

valor = int(input("Digite o valor a sacar [de 10 a 600]: "))
if valor >= 10 and valor <= 600:
    notas_100 = valor // 100
    sobra_de_100 = valor % 100
    notas_50 = sobra_de_100 // 50
    sobra_de_50 = sobra_de_100 % 50
    notas_10 = sobra_de_50 // 10
    sobra_de_10 = sobra_de_50 % 10
    notas_5 = sobra_de_10 // 5
    sobra_de_5 = sobra_de_10 % 5
    notas_1 = sobra_de_5

    print()

    if notas_100 > 0:
        print(f"Notas de R$ 100: {notas_100}")

    if notas_50 > 0:
        print(f"Notas de R$ 50: {notas_50}")

    if notas_10 > 0:
        print(f"Notas de R$ 10: {notas_10}")

    if notas_5 > 0:
        print(f"Notas de R$ 5: {notas_5}")

    if notas_1 > 0:
        print(f"Notas de R$ 1: {notas_1}")

    print()
else:
    print("\nErro! Digite um valor entre R$ 10.00 e R$ 600.00")
