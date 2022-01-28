"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
04. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
--------------------------------------------------------------------------------
"""

print("\n* * * * Vogal ou Consoante * * * *\n")

letra = input("Digite uma letra: ").lower()

# Esta maneira mais direta, mas creio que o objetivo deste exercício é usar apenas
# as estruturas de decisão, então darei as duas maneiras

# 1
print("\nManeira 01 - Simples")

if letra in ["a", "e", "i", "o", "u"]:
    print(f"\n{letra} é uma vogal!\n")
else:
    print(f"\n{letra} é uma consoante\n")

# 2
print("Maneira 02 - Mais verbosa")

if (letra == "a") or (letra == "e") or letra == "i" or letra == "o" or letra == "u":
    print(f"\n{letra} é uma vogal!\n")
else:
    print(f"\n{letra} é uma consoante\n")
