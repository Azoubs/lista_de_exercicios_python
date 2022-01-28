"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 30.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar
    se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo,
    se o mesmo é: equilátero, isósceles ou escaleno.
        Dicas:
    -> Três lados formam um triângulo quando a soma de quaisquer dois lados for
       maior que o terceiro;
    -> Triângulo Equilátero: três lados iguais;
    -> Triângulo Isósceles: quaisquer dois lados iguais;
    -> Triângulo Escaleno: três lados diferentes;
--------------------------------------------------------------------------------
"""

print("\n* * * * Valida Triângulo * * * *\n")

lado_1 = int(input("Digite o primeiro lado: "))
lado_2 = int(input("Digite o segundo lado: "))
lado_3 = int(input("Digite o terceiro lado: "))

if (lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) + lado_2 and (lado_2 + lado_3) > lado_1:
    print("\nTriângulo válido!")

    if lado_1 == lado_2 and lado_1 == lado_3:
        print("\nTriângulo equilátero.\n")
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("\nTriângulo Isósceles.\n")
    elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
        print("\nTriângulo Escaleno.\n")
else:
    print("\nTriângulo inválido!\n")
