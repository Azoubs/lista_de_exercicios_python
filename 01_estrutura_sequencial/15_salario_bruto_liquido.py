"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
    trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
    sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
    5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
    Obs.: Salário Bruto - Descontos = Salário Líquido.
--------------------------------------------------------------------------------
"""

print("\n* * * * Salário Líquido * * * *\n")

salario_hora = float(input("Digite o valor recebido por hora: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
salario_bruto = salario_hora * horas_trabalhadas
desconto_ir = (11/100) * salario_bruto
desconto_inss = (8/100) * salario_bruto
desconto_sindicato = (5/100) * salario_bruto
salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindicato

print("\n* * * * Resumo * * * *\n")

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"- desconto IR (11%): R${desconto_ir:.2f}")
print(f"- deconto INSS (8%): R${desconto_inss:.2f}")
print(f"- sindicato (5%): R${desconto_sindicato:.2f}")
print(f"\nSalário líquido: R${salario_liquido:.2f}\n")
