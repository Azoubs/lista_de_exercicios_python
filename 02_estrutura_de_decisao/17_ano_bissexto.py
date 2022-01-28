"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 02.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
17. Faça um Programa que peça um número correspondente a um determinado ano e em
    seguida informe se este ano é ou não bissexto.
--------------------------------------------------------------------------------
"""

print("\n* * * * Ano Bissexto * * * *\n")

ano = int(input("Digite o ano: "))

if (ano % 4 == 0) and (ano % 100 != 0):
    print(f"\n{ano} é bissexto!\n")
elif (ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0):
    print(f"\n{ano} é bissexto!\n")
else:
    print(f"\n{ano} não é bissexto!\n")
