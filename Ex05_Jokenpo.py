# Jokenpo

import random, os

def placar():
    if contador > 0:
        print("\nPLACAR ATUAL")
        print(f"EMPATES: {empate}")
        print(f"MÁQUINA: {vitoriasmaquina}")
        print(f"JOGADOR: {vitoriasjogador}")
    else:
        print("\nPLACAR FINAL!")
        print(f"EMPATES: {empate}")
        print(f"MÁQUINA: {vitoriasmaquina}")
        print(f"JOGADOR: {vitoriasjogador}")

def placarfinal():
    if vitoriasjogador > vitoriasmaquina:
        print("Parabéns! Você venceu!")
    elif vitoriasjogador == vitoriasmaquina:
        print("O jogo terminou empatado")
    else:
        print("Você perdeu! A máquina ganhou o jogo!")

while True:
    print("\nJOKENPO\n")
    print("Ataques disponíveis:")
    print("[1] Pedra")
    print("[2] Papel")
    print("[3] Tesoura\n")

    contador = 10
    vitoriasmaquina = 0
    vitoriasjogador = 0
    empate = 0

    while contador > 0:
            maquina = random.randrange(1,3)
            
            ataque = int(input("Escolha o seu ataque [1 - Pedra], [2 - Papel], [3 - Tesoura]: "))
            while ataque != 1 or ataque != 2 or ataque != 3:
                print("Você escolheu um ataque inexistente. Tente novamente!\n")
                ataque = int(input("Escolha o seu ataque [1 - Pedra], [2 - Papel], [3 - Tesoura]: "))
            
            contador -= 1

            if maquina == ataque:
                print("\nVocês escolheram o mesmo ataque. EMPATE!")
                empate +=1
            elif maquina == 1 and ataque == 2:
                print("\nO jogador escolheu PAPEL e a máquina escolheu PEDRA. Vitória do JOGADOR!")
                vitoriasjogador +=1
            elif maquina == 1 and ataque == 3:
                print("\nO jogador escolheu TESOURA e a máquina escolheu PEDRA. Vitória da MÁQUINA!")
                vitoriasmaquina +=1
            elif maquina == 2 and ataque == 1:
                print("\nO jogador escolheu PEDRA e a máquina escolheu PAPEL. Vitória da MÁQUINA!")
                vitoriasmaquina +=1
            elif maquina == 2 and ataque == 3:
                print("\nO jogador escolheu TESOURA e a máquina escolheu PAPEL. Vitória do JOGADOR!")
                vitoriasjogador +=1
            elif maquina == 3 and ataque == 1:
                print("\nO jogador escolheu PEDRA e a máquina escolheu TESOURA. Vitória do JOGADOR!")
                vitoriasjogador +=1
            else:
                print("\nO jogador escolheu PAPEL e a máquina escolheu TESOURA. Vitória da MÁQUINA!")
                vitoriasmaquina +=1
            
            placar()

            print(f"Partidas restantes: {contador}")

    placarfinal()    

    confirma = input("\nDeseja jogar novamente? [S/N]: ")
    if confirma == 'n' or confirma == 'N':
        break
    else:
        os.system('cls')



    
        
                

        