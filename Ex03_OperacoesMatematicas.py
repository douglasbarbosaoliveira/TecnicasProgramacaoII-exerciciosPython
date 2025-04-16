# Exercício de operadores matemáticos

import random, os

contador = 0
acertos = 0
erros = 0

def placar():
    print(f"\nQuantidade de acertos: {acertos}")
    print(f"Quantidade de erros: {erros}\n")

while True:

    print("Exercício de operações matemáticas\n")

    n1 = random.randrange(1,10)
    n2 = random.randrange(1,10)
    operacao = random.randrange(1,3)
    contador +=1
    print("\nNova operação matemática!\n")
    if operacao == 1:
        resultado = n1 + n2
        print(f"{n1} + {n2} = ")
    elif operacao == 2:
        resultado = n1 -n2
        print(f"{n1} - {n2} = ")
    else:
        resultado = n1 * n2
        print(f"{n1} x {n2} = ")

    entrada = int(input("\nDigite o resultado da operação: "))

    if resultado == entrada:
        print(f"\nVocê acertou! O valor da operação matemática é {resultado}")
        acertos +=1
    else:
        print(f"\nVocê errou! O valor da operação matemática é {resultado} e não {entrada}")
        erros +=1

    placar()

    confirma = input("\nDeseja continuar? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')

    

    



