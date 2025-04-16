# Black Jack - 21
'''
♥♦♣♠ #Alt + 3 ou 4 ou 5 ou 6
'''

import random, os

vitoriasjogador = 0
vitoriasmaquina = 0

while True:
    cartasjogador = []
    naipecartasjogador = []
    cartasmaquina = []
    naipecartasmaquina = []

    print("Blackjack 21")

    for i in range(3):
        CartaJogador = random.randrange(1,14)
        if CartaJogador > 10:
            cartasjogador.append(10)
            if  CartaJogador == 11:
                naipeCarta = "J"
                naipecartasjogador.append(naipeCarta)
            elif CartaJogador == 12:
                naipeCarta = "Q"
                naipecartasjogador.append(naipeCarta)
            else:
                naipeCarta = "K"
                naipecartasjogador.append(naipeCarta)
        else:
            cartasjogador.append(CartaJogador)
            if CartaJogador == 1:
                naipeCarta = "A"
                naipecartasjogador.append(naipeCarta)
            else:
                naipeCarta = CartaJogador
                naipecartasjogador.append(CartaJogador)

        CartaMaquina = random.randrange(1,14)
        if CartaMaquina > 10:
            cartasmaquina.append(10)
            if CartaMaquina == 11:
                naipeCarta = "J"
                naipecartasmaquina.append(naipeCarta)
            elif CartaMaquina == 12:
                naipeCarta = "Q"
                naipecartasmaquina.append(naipeCarta)
            else:
                naipeCarta = "K"
                naipecartasmaquina.append(naipeCarta)
        else:
            cartasmaquina.append(CartaMaquina)
            if CartaMaquina == 1:
                naipeCarta = "A"
                naipecartasmaquina.append(naipeCarta)
            else:
                naipeCarta = CartaMaquina
                naipecartasmaquina.append(CartaMaquina)

    print("\nCartas Jogador:")
    for i in naipecartasjogador:
        print(f"{i} ♥")

    print("\nCartas Máquina:")
    for i in naipecartasmaquina:
        print(f"{i} ♣")

        
    totalJogador = sum(cartasjogador)
    totalMaquina = sum(cartasmaquina)

    print(f"\nJogador: {totalJogador} pontos")
    print(f"Máquina: {totalMaquina} pontos\n")


    if totalJogador > 21 or totalMaquina > 21:
        if totalJogador > totalMaquina and totalMaquina < 22:
            print(f"MÁQUINA VENCEU! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
            vitoriasmaquina +=1
        elif totalJogador < totalMaquina and totalJogador < 22:
            print(f"JOGADOR VENCEU! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
            vitoriasjogador +=1
        else:
            print(f"AMBOS PERDERAM! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
    else:
        if totalJogador > totalMaquina:
            print(f"JOGADOR VENCEU! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
            vitoriasjogador +=1
        elif totalJogador == totalMaquina:
            print(f"EMPATE! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
        else:
            print(f"MÁQUINA VENCEU! O jogador fez {totalJogador} pontos e a máquina fez {totalMaquina} pontos.")
            vitoriasmaquina +=1

    print("\nPLACAR GERAL")
    print(f"VITÓRIAS JOGADOR: {vitoriasjogador}")
    print(f"VITÓRIAS MÁQUINA: {vitoriasmaquina}")

    
    confirma = input("\nDeseja continuar jogando? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')

    

