import random
import os

erros = 0
sorteado = random.randrange(0,100)
jogador = int(input("Digite o seu número: "))

while (sorteado != jogador):
    os.system('cls')

    if(sorteado > jogador):
        print("ERROU, o número é maior")
    else:
        print("ERROU, o número é menor")
    
    erros += 1
    jogador = int(input("Digite seu número: "))

print("Numero {}, você acertou em {} tentativas".format(jogador, erros))