"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
    perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?"
    O programa deve no final emitir uma classificação sobre a participação da
    essoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
    classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
    Caso contrário, ele será classificado como "Inocente".
--------------------------------------------------------------------------------
"""

print("\n* * * * Crime * * * *\n")

num_questoes = 0

# Poderia adicionar as respostas ao num_questoes, visto que são 0 e 1
# Mas utilizando os ifs, fica mais seguro
telefone = int(input("Telefonou para a vítima? [1 - sim | 0 - não]: "))
if telefone == 1:
    num_questoes += 1

local = int(input("Esteve no local do crime? [1 - sim | 0 - não]: "))
if local == 1:
    num_questoes += 1

mora_perto = int(input("Mora perto da vítima? [1 - sim | 0 - não]: "))
if mora_perto == 1:
    num_questoes += 1

devia = int(input("Devia para a vítima? [1 - sim | 0 - não]: "))
if devia == 1:
    num_questoes += 1

trabalhou = int(input("Trabalhou com a vítima? [1 - sim | 0 - não]: "))
if trabalhou == 1:
    num_questoes += 1

if num_questoes == 2:
    print("\nPessoa suspeita!\n")
elif num_questoes > 2 and num_questoes < 5:
    print("\nCúmplice!\n")
elif num_questoes == 5:
    print("\nASSASSINO!\n")
else:
    print("\nInocente\n")
