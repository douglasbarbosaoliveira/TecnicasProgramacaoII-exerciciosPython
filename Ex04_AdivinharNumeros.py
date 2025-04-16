# Adivinhar números

import random, os

contador = 5
sorteado = random.randrange(1,50)

while True:

    print("Jogo da adivinhação dos números!\n")

    while contador > 0:
        numero = int(input("\nDigite um número entre 01 e 50: "))
        while numero < 1 or numero > 50:
            print("Você escolheu um número inválido. Tente novamente!")
            numero = int(input("\nDigite um número entre 01 e 50: "))

        if numero < sorteado:
            print("Digite um número maior! ")
            contador -=1
        elif numero > sorteado:
            print("Digite um número menor! ")
            contador -=1
        else:
            print(f"Parabéns. Você acertou! O número sorteado foi {sorteado}")
            break

        if contador > 0:
            print(f"Você possui mais {contador} tentativas!")
            continue
        else:
            print(f"\nVocê perdeu. O número escolhido foi {sorteado}")
            break

    confirma = input("\nDeseja jogar novamente? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')

        
