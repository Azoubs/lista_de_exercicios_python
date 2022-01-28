"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
--------------------------------------------------------------------------------
"""

print("\n* * * * Várias Operações * * * *\n")

int_1 = int(input("Digite o primeiro número inteiro: "))
int_2 = int(input("Digite o segundo número inteiro: "))
real_1 = float(input("Digite um número real: "))

print(f"\nProduto do dobro do primeiro com metade do segundo: {(2 * int_1) * (int_2 / 2)}")
print(f"Soma do triplo do primeiro com o terceiro: {(3 * int_1) + real_1}")
print(f"Terceiro elevado ao cubo: {real_1 ** 3}\n")
