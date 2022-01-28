"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
    o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
    maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
    (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
    que você faça um programa que leia a variável peso (peso de peixes) e calcule
    o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
    na variável multa o valor da multa que João deverá pagar. Imprima os dados do
    programa com as mensagens adequadas.
--------------------------------------------------------------------------------
"""

# Estou considerando que o valor do peso sempre será acima de 50, do contrário,
#   teria que usar estruturas de decisão, que não é a proposta (na minha inter-
#   pretação) desta parte dos exercícios 

print("\n* * * * Multa! * * * *\n")

peso_pescado = float(input("Digite o peso dos peixes: "))
limite = 50
excesso = peso_pescado - limite
multa = excesso * 4

print(f"\nA multa será de: R$ {multa:.2f}\n")
