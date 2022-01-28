"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
05. Faça um programa para a leitura de duas notas parciais de um aluno. O programa
    deve calcular a média alcançada por aluno e apresentar:
    -> A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    -> A mensagem "Reprovado", se a média for menor do que sete;
    -> A mensagem "Aprovado com Distinção", se a média for igual a dez.
--------------------------------------------------------------------------------
"""

print("\n* * * * Aprovado ou Reprovado * * * *\n")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if media >= 7 and media < 10:
    print("\nAluno Aprovado.\n")
elif media < 7:
    print("\nAluno Reprovado.\n")
elif media == 10:
    print("\nAluno Aprovado com Distinção.\n")
