"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar
    M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
    "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
--------------------------------------------------------------------------------
"""

print("\n* * * * Turnos * * * *\n")

turno = input("Digite o seu turno [M/V/N]: ").upper()

if turno == "M":
    print("\nBom dia!\n")
elif turno == "V":
    print("\nBoa tarde!\n")
elif turno == "N":
    print("\nBoa noite!\n")
else:
    print("\nTurno inválido!\n")
