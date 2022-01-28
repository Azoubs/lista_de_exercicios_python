"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura de Decisão
Fonte: https://wiki.python.org.br/EstruturaDeDecisao
Data: 03.01.2022
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
    Confira:
                              Até 5 Kg           Acima de 5 Kg
        File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
        Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
        Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
    Para atender a todos os clientes, cada cliente poderá levar apenas um dos
    tipos de carne da promoção, porém não há limites para a quantidade de carne
    por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda
    um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
    e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
    as informações da compra: tipo e quantidade de carne, preço total, tipo de
    pagamento, valor do desconto e valor a pagar.
--------------------------------------------------------------------------------
"""

print("\n* * * * Carnes * * * *\n")

print("""
-> CARNES <-

1. Filé Duplo
2. Alcatra
3. Picanha
""")

carne = int(input("Selecione a carne desejada [1-3]: "))
desconto, valor_bruto, valor_final, carne_nome, desconto_msg = 0, 0, 0, "", ""

if carne > 0 and carne < 4:
    peso = int(input("Digite o peso (em kgs) a comprar: "))
    cartao = int(input("Compra com cartão? [1 - Sim | 0 - Não]: "))
    if carne == 1:
        carne_nome = "Filé Duplo"
        if peso <= 5:
            carne_kg = 4.9
        else:
            carne_kg = 5.8
    elif carne == 2:
        carne_nome = "Alcatra"
        if peso <= 5:
            carne_kg =  5.9
        else:
            carne_kg = 6.8
    elif carne == 3:
        carne_nome = "Picanha"
        if peso <= 5:
            carne_kg = 6.9
        else:
            carne_kg = 7.8
    valor_bruto = peso * carne_kg
    if cartao == 1:
        desconto = (5/100) * valor_bruto
        desconto_msg = "Desconto de 5%!"
    else:
        desconto_msg = "SEM DESCONTO"
    valor_final = valor_bruto - desconto

    print("\n* * * * VALOR FINAL * * * *\n")
    print(f"{desconto_msg}")
    print(f"Valor de desconto: R${desconto:.2f}")
    print(f"Valor final: R${valor_final:.2f}\n")
else:
    print("\nErro\n")
