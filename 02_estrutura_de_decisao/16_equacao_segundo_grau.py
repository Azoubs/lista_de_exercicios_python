"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 02.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na
    forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
    as consistências, informando ao usuário nas seguintes situações:
    a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo
       grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    b. Se o delta calculado for negativo, a equação não possui raizes reais.
       Informe ao usuário e encerre o programa;
    c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
       informe-a ao usuário;
    d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
--------------------------------------------------------------------------------
"""
import math

print("\n* * * * Equação do Segundo Grau * * * *\n")

a = int(input("Digite o primeiro valor: "))

if a != 0:
    b = int(input("Digite o segundo valor: "))
    c = int(input("Digite o terceiro valor: "))
    delta = (b ** 2) - (4 * a * c)
    if delta > 0:
        x1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
        x2 = ((b * -1) - math.sqrt(delta)) / (2 * a)

        print("\nEquação possui duas raízes reais")
        print(f"x': {x1}")
        print(f"x'': {x2}\n")
    elif delta == 0:
        x = ((b * -1) + math.sqrt(delta)) / (2 * a)
        print(f"\nEquação possui apenas uma raiz real: {x:.1f}")
    else:
        print("\nEquação não possui raízes reais.\nFim do programa.\n")
else:
    print("\nA equação não é do segundo grau.\nFim do programa.\n")
