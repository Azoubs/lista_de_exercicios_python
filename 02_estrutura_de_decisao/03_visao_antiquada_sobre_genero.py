"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
03. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme
    a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
--------------------------------------------------------------------------------
"""

print("\n* * * * Gêneros * * * *\n")

sexo = input("Digite o seu gênero [M/F]: ").upper()

if sexo == "M":
    print("\nMasculino.\n")
elif sexo == "F":
    print("\nFeminino.\n")
else:
    print("\nOutro.\n")
