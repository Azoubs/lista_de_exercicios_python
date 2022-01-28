"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 02.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quan-
    tidade de centenas, dezenas e unidades do mesmo. Observando os termos no plu-
    ral a colocação do "e", da vírgula entre outros.
        Exemplo:
    -> 326 = 3 centenas, 2 dezenas e 6 unidades
    -> 12 = 1 dezena e 2 unidades
    Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
                11, 1, 7 e 16
--------------------------------------------------------------------------------
"""

print("\n* * * * Centenas, Dezenas e Unidades * * * *\n")

while True:
    numero = int(input("Digite um número: "))

    tem_centena, tem_dezena, tem_unidade = False, False, False
    msg_centena, msg_dezena, msg_unidade = "", "", ""

    if numero < 1000:
        centenas = numero // 100
        sobra_de_centenas = numero % 100
        dezenas = sobra_de_centenas // 10
        sobra_de_dezenas = sobra_de_centenas % 10
        unidades = sobra_de_dezenas

        if centenas > 0:
            tem_centena = True
        if dezenas > 0:
            tem_dezena = True
        if unidades > 0:
            tem_unidade = True

        if tem_centena and tem_dezena and tem_unidade:
            if centenas == 1:
                msg_centena = "1 centena,"
            else:
                msg_centena = f"{centenas} centenas,"

            if dezenas == 1:
                msg_dezena = "1 dezena e"
            else:
                msg_dezena = f"{dezenas} dezenas e"

            if unidades == 1:
                msg_unidade = "1 unidade."
            else:
                msg_unidade = f"{unidades} unidades."
            print(msg_centena, msg_dezena, msg_unidade)

        if tem_centena and not tem_dezena and not tem_unidade:
            if centenas == 1:
                msg_centena = "1 centena."
            else:
                msg_centena = f"{centenas} centenas."
            print(msg_centena)

        if tem_centena and tem_dezena and not tem_unidade:
            if centenas == 1:
                msg_centena = "1 centena e"
            else:
                msg_centena = f"{centenas} centenas e"

            if dezenas == 1:
                msg_dezena = "1 dezena."
            else:
                msg_dezena = f"{dezenas} dezenas."
            print(msg_centena, msg_dezena)

        if tem_centena and not tem_dezena and tem_unidade:
            if centenas == 1:
                msg_centena = "1 centena e"
            else:
                msg_centena = f"{centenas} centenas e"

            if unidades == 1:
                msg_unidade = "1 unidade."
            else:
                msg_unidade = f"{unidades} unidades."
            print(msg_centena, msg_unidade)

        if not tem_centena and tem_dezena and tem_unidade:
            if dezenas == 1:
                msg_dezena = "1 dezena e"
            else:
                msg_dezena = f"{dezenas} dezenas e"

            if unidades == 1:
                msg_unidade = "1 unidade."
            else:
                msg_unidade = f"{unidades} unidades."
            print(msg_dezena, msg_unidade)

        if not tem_centena and tem_dezena and not tem_unidade:
            if dezenas == 1:
                msg_dezena = "1 dezena."
            else:
                msg_dezena = f"{dezenas} dezenas."
            print(msg_dezena)

        if not tem_centena and not tem_dezena and tem_unidade:
            if unidades == 1:
                msg_unidade = "1 unidade."
            else:
                msg_unidade = f"{unidades} unidades."
            print(msg_unidade)

    sair = int(input("\nDigite 0 para sair: "))
    print()
    if sair == 0:
        break
