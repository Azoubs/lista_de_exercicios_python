"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 02.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
    mesma é uma data válida.
--------------------------------------------------------------------------------
"""

print("\n* * * * Valida Data * * * *\n")

dia = int(input("Digite um dia: "))

if dia > 0 and dia < 31:
    mes = int(input("Digite um mês: "))
    if mes > 0 and mes < 13:
        ano = int(input("Digite um ano: "))
        print(f"\n{dia}\{mes}\{ano}\n")
    else:
        print("\nMês inválido!")
else:
    print("\nDia inválido!")
