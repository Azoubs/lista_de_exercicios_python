"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
20. Faça um Programa para leitura de três notas parciais de um aluno. O programa
    deve calcular a média alcançada por aluno e presentar:
    a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
        média alcançada;
    b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
       média alcançada;
    c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
--------------------------------------------------------------------------------
"""

print("\n* * * * Média Alunos * * * *\n")

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7 and media < 10:
    print("\nAluno aprovado!")
    print(f"Média: {media:.1f}\n")
elif media < 7:
    print("\nAluno reprovado!")
    print(f"Média: {media:.1f}\n")
elif media == 10:
    print("\nAluno Aprovado com Distinção!")
    print(f"Média: {media:.1f}\n")
else:
    print("\nErro\n")
