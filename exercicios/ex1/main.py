import os

carros = []

class Carro:
    nome = ""
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = (int(pot))*2
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
    
    def info(self):
        print(f"Nome.......: {self.nome}")
        print(f"Potência...: {self.pot}")
        print(f"Vel. Máxima: {self.velMax}")
        print("Ligado.....: " + ("Sim" if self.ligado == True else "Não"))
        print("-------------------------------\n")

def menu():
    os.system("cls") or None
    print("---------- MENU ------------")
    print("1 - Novo carro")
    print("2 - Informações do carro")
    print("3 - Excluir carro")
    print("4 - Ligar carro")
    print("5 - Desligar carro")
    print("6 - Mostrar todos os carros")
    print("7 - Sair")
    print("----------------------------\n")

    
    opc = int(input("Digite uma opção: "))
    return opc

def novo():
    os.system("cls") or None

    n = input("Nome do carro: ")
    p = input("Potência do carro: ")
    car = Carro(n, p)

    carros.append(car)
    print("Novo carro registrado\n")

    os.system("pause") # pausa e espera o clique de uma tecla

def inform():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ver as informações: "))

    try:
        print("-------------------------------")
        carros[n].info()
    except:
        print("Carro não existente\n")
    
    os.system("pause")

def excluir():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja excluir: "))

    try:
        del carros[n]
        print("Carro deletado com sucesso\n")

    except:
        print("Carro não existente\n")
    
    os.system("pause")

def ligarCarro():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ver as informações: "))

    try:
        carros[n].ligar()
        print(f"Carro {n} ligado\n")

    except:
        print("Carro não existente\n")
    
    os.system("pause")

def desligarCarro():
    os.system("cls") or None
    n = int(input("Informe o número do carro que deseja ver as informações: "))

    try:
        carros[n].desligar()
        print(f"Carro {n} desligado\n")
    except:
        print("Carro não existente\n")
    
    os.system("pause")

def listar():
    os.system("cls") or None
    p = 0

    for c in carros:
        print(f"{p} - {c.nome}")

    os.system("pause")

ret = menu()
while ret < 7:
    if ret == 1:
        novo()
    elif ret == 2:
        inform()
    elif ret == 3:
        excluir()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        listar()
    else:
        print("Opção inválida\n")
    
    ret = menu()

os.system("cls")
print("Programa finalizado")