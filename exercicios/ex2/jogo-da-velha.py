import os
import random
from colorama import Fore, Back, Style # fore: cor da fonte / back: fundo / style: tipo da fonte

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

jogarNovamente = True
jogadas = 0
quemJoga = 1 # 1 = Jogador 1 | 2 = CPU / Jogador 2
maxJogadas = 9
vit = False
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha

    os.system("cls") or None

    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2] + "\n")
    print(f"Jogadas: { Fore.BLUE + str(jogadas) + Fore.RESET }")

def jogador1():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga == 1 and jogadas < maxJogadas:
        l=int(input("Linha..: "))
        c=int(input("Coluna.: "))

        try:
            while velha[l][c] != " ":
                l=int(input("Linha..: "))
                c=int(input("Coluna.: "))

            velha[l][c] = "X"
            quemJoga = 2
            jogadas+=1
        except:
            print("Linha e/ou coluna inválida\n")
            os.system("pause")

def cpu():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)

        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        
        velha[l][c] = "O"
        jogadas+=1
        quemJoga = 1

def vitoria(): 
    # 3 possibilidades de vitoria em coluna = c0 l0 l1 l2| c1 l0 l1 l2 | c2 l0 l1 l2
    # 3 possibilidades de vitoria em linha = l0 c0 c1 c2 | l1 c0 c1 c2 | l2 c0 c1 c2
    # 2 possibilidades de vitoria em horizontal = l0 c0 l1 c1 l2 c2 | l0 c2 l1 c1 l2 c0
    #     print("")

# loop principal do jogo
while True: # loop infinito, somente para quando executar break
    tela()
    jogador1()
    cpu()

