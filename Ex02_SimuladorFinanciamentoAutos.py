# Financiamento de veículos

# Entrada de dados: Valor do automóvel; Valor de entrada; Plano de pagamento (12, 24, 36 ou 48 meses); Ano do veículo
#                   Taxas de juros: 12 meses = 12.8%; 24 meses = 24.5%; 36 meses = 32.4%; 48 meses - 41.7%
# Saída de dados: Valor financiado; Plano de Pagamento escolhido; Valor da parcela mensal com juros inclusos; 
#                 IPVA: 4% (Veículos anteriores a 1995: Isentos); Total global da operação


import os

while True: 

    print("Simulador - Financiamento de automóveis")

    valorAuto = float(input("\nDigite em reais o valor do automóvel: R$ "))
    while valorAuto < 1000 or valorAuto> 1000000000:
        print("Valor incorreto. Tente novamente!")
        valorAuto = float(input("\nDigite em reais o valor do automóvel: R$ "))

    anoVeiculo = int(input("Digite o ano do veículo: "))
    while anoVeiculo < 1950 or anoVeiculo > 2025:
        print("Ano inválido. Digite valores entre 1950 e 2025.")
        anoVeiculo = int(input("Digite o ano do veículo: "))

    if anoVeiculo > 1995:
        ipva = valorAuto * 0.04
    else:
        ipva = 0

    valorEntrada = float(input("\nDigite em reais o valor da entrada: R$ "))
    while valorEntrada <0 or valorEntrada >= valorAuto:
        print("O valor da entrada deve ser inferior ao valor de tabela do veículo. Insira novamente!")
        valorEntrada = float(input("\nDigite em reais o valor da entrada: R$ "))
    valorRestante = valorAuto - valorEntrada



    financiamento = int(input("\nEscolha a quantidade de parcelas do financiamento (12, 24, 36 ou 48 vezes?): "))
    while financiamento != 12 and financiamento !=24 and financiamento != 36 and financiamento != 48:
        print("Valor inválido de parcelas. Tente novamente!")
        financiamento = int(input("\nEscolha a quantidade de parcelas do financiamento (12, 24, 36 ou 48 vezes?): "))

    # Cálculo do valor das parcelas
    if financiamento == 12:
        valorfinanciado = valorRestante * 1.128
        parcelas = valorfinanciado/financiamento
    elif financiamento == 24:
        valorfinanciado = valorRestante * 1.245
        parcelas = valorfinanciado/financiamento
    elif financiamento == 36:
        valorfinanciado = valorRestante * 1.324
        parcelas = valorfinanciado/financiamento
    else:
        valorfinanciado = valorRestante * 1.417
        parcelas = valorfinanciado/financiamento

    totalOperacao = valorEntrada + valorfinanciado + ipva

    print("\n-------------------------------------------------------------------------------------------")
    print("\nDados do pagamento:\n")
    print(f"Valor total do veículo: R$ {valorAuto:.2f}")
    print(f"Valor do IPVA: R$ {ipva:.2f}")
    print(f"Valor a ser financiado: R$ {valorRestante:.2f}")
    print(f"Modalidade de financiamento: {financiamento} vezes")
    print(f"Juros do financimento: R$ {valorfinanciado - valorRestante:.2f}")
    print(f"Valor mensal de cada parcela: R$ {parcelas:.2f}")
    print(f"Valor total da operação: R$ {totalOperacao:.2f}")

    confirma = input("\nDeseja realizar uma nova consulta? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')