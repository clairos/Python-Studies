import os
import random
from colorama import Fore, Back, Style 

# fore: cor da fonte / back: fundo / style: tipo da fonte

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

jogarNovamente = "s"
jogadas = 0
jog = 0 # 1 = jogador 2 | 2 = CPU
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
        l = int(input("Linha..: "))
        c = int(input("Coluna.: "))

        try:
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))

            velha[l][c] = "X"
            jogadas += 1
            quemJoga = 2

        except:
            print("Linha e/ou coluna inválida\n")
            os.system("pause")

def jogador2():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        tela()
        l = int(input("Linha..: "))
        c = int(input("Coluna.: "))

        try:
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))

            velha[l][c] = "O"
            jogadas += 1
            quemJoga = 1

        except:
            print("Linha e/ou coluna inválida\n")
            os.system("pause")

def cpu():
    global jogadas
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga == 2 and jogadas < maxJogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)

        while velha[l][c] != " ":
            l = random.randrange(0,3) #entre 0 e menor que 3 -> 0, 1 e 2
            c = random.randrange(0,3)
        
        velha[l][c] = "O"
        jogadas += 1
        quemJoga = 1

def checkVitoria(): 
    # 3 possibilidades de vitoria em coluna = c0 l0 l1 l2| c1 l0 l1 l2 | c2 l0 l1 l2
    # 3 possibilidades de vitoria em linha = l0 c0 c1 c2 | l1 c0 c1 c2 | l2 c0 c1 c2
    # 2 possibilidades de vitoria em horizontal = l0 c0 l1 c1 l2 c2 | l0 c2 l1 c1 l2 c0
    global velha
    vitoria = False
    symbols = ["X","O"] 

    for s in symbols:
        vitoria = 'n'

        # verifica vitoria em linha
        il = ic = 0 # il => indice de linha | ic => indice de coluna

        while il < 3: #coracaozinho hehe
            soma = 0
            ic = 0

            while ic < 3: #coracaozinho dinovo
                if(velha[il][ic] == s): # s vem do for
                    soma += 1

                ic += 1

            if(soma == 3):
                vitoria = s
                break

            il += 1 

        if(vitoria != 'n'):
            break
        
        #verifica vitoria em coluna
        il = ic = 0 

        while ic < 3: 
            soma = 0
            il = 0

            while il < 3: # hihi
                if(velha[il][ic] == s):
                    soma += 1

                il += 1
 
            if(soma == 3):
                vitoria = s
                break

            ic += 1

        if(vitoria != 'n'):
            break

        # verifica vitoria em diagonal 1
        soma = 0
        idg = 0

        while idg < 3:
            if (velha[idg][idg] == s):
                soma += 1

            idg += 1

        if(soma == 3):
            vitoria = s
            break

        # verifica vitoria em diagonal 2
        soma = 0
        idgl = 0 # idgl = indice de diagonal linha 
        idgc = 2 # idgc = indice de diagonal coluna

        while idgc >= 0:
            if(velha[idgl][idgc] == s):
                soma += 1

            idgl += 1
            idgc -= 1

        if(soma == 3):
            vitoria = s
            break
    
    return vitoria
        
def reset():
    global velha
    global jogadas
    global jog
    global quemJoga
    global maxJogadas
    global vit

    jogadas = 0
    jog = 0
    quemJoga = 1 # 1 = Jogador 1 | 2 = CPU / Jogador 2
    maxJogadas = 9
    vit = ""
    velha = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


# loop principal do jogo
while(jogarNovamente == "s" or jogarNovamente == "S"):
    jog = int(input("Digite 1 para jogar com um amigo, 2 para jogar contra a CPU: "))

    while True: # loop infinito, somente para quando executar break
        tela()
        jogador1()

        if(jog == 1):
            jogador2()
        else:
            cpu()

        tela()
        vit = checkVitoria()

        if(vit != 'n') or (jogadas >= maxJogadas):
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.GREEN)

    if(vit == "X" or vit == "O"):
        print("Resultado: Jogador " + Fore.YELLOW + vit + Fore.GREEN + " venceu!") 
    else:
        print("Resultado: EMPATE")
    
    jogarNovamente = input(Fore.MAGENTA+"Jogar novamente? [s/n]: " + Fore.RESET)

    reset();
