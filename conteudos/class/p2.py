# POO

import os

class Carro: # valores default caso nao seja atribuido
    os.system("cls")

    velMax = 0
    ligado = False
    cor = ""

    def __init__(self,v,l,c): # definicao de construtor
        self.velMax = v # self. = this.
        self.ligado = l
        self.cor = c

    def mostrar(self):
        print(f"Velocidade máxima: {self.velMax}")
        print(f"Cor..............: {self.cor}")
        estado="sim" if self.ligado else "não"
        print(f"Ligado...........: {estado}")
        print("---------------------------")

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")

c1=Carro(200,False, "Prata")
c2=Carro(120, False, "Preto")
c3=Carro(400, False, "Vermelho")

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()