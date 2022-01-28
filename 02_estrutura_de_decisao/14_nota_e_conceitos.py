"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa
    disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
    conceitos obedece à tabela abaixo:
          Média de Aproveitamento  Conceito
          Entre 9.0 e 10.0        A
          Entre 7.5 e 9.0         B
          Entre 6.0 e 7.5         C
          Entre 4.0 e 6.0         D
          Entre 4.0 e zero        E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
    e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
    conceito for D ou E.
--------------------------------------------------------------------------------
"""

print("\n* * * * Nota & Conceitos * * * *\n")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2
conceito, situacao = None, None

if media >= 9 and media <= 10:
    conceito = "A"
    situacao = "Aprovado!"
elif media < 9 and media >= 7.5:
    conceito = "B"
    situacao = "Aprovado!"
elif media < 7.5 and media >= 6:
    conceito = "C"
    situacao = "Aprovado!"
elif media < 6 and media >= 4:
    conceito = "D"
    situacao = "Reprovado!"
elif media < 4:
    conceito = "E"
    situacao = "Reprovado!"

print(f"\nMédia: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Aluno {situacao}\n")
