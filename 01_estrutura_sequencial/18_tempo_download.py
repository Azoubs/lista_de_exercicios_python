"""
* * * * L I S T A - D E - E X E R C Í C I O S * * * *

Estrutura Sequencial
Fonte: https://wiki.python.org.br/EstruturaSequencial
Data: 29.12.2021
Estudante: Filipe Azoubel
--------------------------------------------------------------------------------
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
    velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
    de download do arquivo usando este link (em minutos).
--------------------------------------------------------------------------------
"""
import math

print("\n* * * * Tempo de Download * * * *\n")

tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_internet = float(input("Digite a velocidade da internet (Mbps): "))

tempo_segundos = tamanho_arquivo / velocidade_internet
tempo_minutos = math.ceil(tempo_segundos / 60)

print(f"Tempo de download aproximado: {tempo_minutos} min\n")
