# Folha de Pagamento

# Entrada de dados: Quantidade de salários
# Saída de dados: Salário Bruto; 
#                 INSS (caso salário bruto seja igual ou superior a R$ 1850,00, alíquota de 11%. Caso contrário, haverá isenção)
#                 Salário líquido;
# Referência: Salário mínino = R$ 1518,00

import os

while True: 
    print("Folha de Pagamento\n")

    qtdeSalarios = int(input("Digite a quantidade de salários mínimos que o funcionário recebe: "))

    salarioBruto = qtdeSalarios * 1518

    if salarioBruto >= 1850:
        calculo = salarioBruto * 0.11
        salarioLiquido = salarioBruto - calculo
        inss_str = str(calculo)
        inss = "R$ " + inss_str
    else:
        inss = "Isento"
        salarioLiquido = salarioBruto

    print("\nDados do pagamento:\n")
    print(f"Salário Bruto: R$ {salarioBruto:.2f}")
    print(f"INSS: {inss}")
    print(f"Salário Líquido: R$ {salarioLiquido:.2f}")

    confirma = input("\nDeseja continuar? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')

