"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
    operação ele deseja realizar. O resultado da operação deve ser acompanhado de
    uma frase que diga se o número é:
    a. par ou ímpar;
    b. positivo ou negativo;
    c. inteiro ou decimal.
--------------------------------------------------------------------------------
"""

print("\n* * * * Operaçõess * * * *\n")

num_1 = float(input("Digite o número: "))
operacao = int(input("""
OPERAÇÕES

1 - Par ou ímpar
2 - Positivo ou negativo
3 - Inteiro ou decimal

Selecione uma opção [1-3]: """))

if operacao == 1:
    if num_1 % 2 == 0:
        print("\nNúmero par!\n")
    else:
        print("\nNúmero ímpar!\n")
elif operacao == 2:
    if num_1 >= 0:
        print("\nNúmero positivo!\n")
    else:
        print("\nNúmero negativo!\n")
elif operacao == 3:
    if num_1 == round(num_1):
        print("\nNúmero inteiro!\n")
    else:
        print("\nNúmero decimal!\n")
else:
    print("\nErro!\n")
