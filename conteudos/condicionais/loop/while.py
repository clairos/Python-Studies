import os

os.system('cls') # limpa a tela

i = 0

while i < 9:
    print(i)
    i += 1
    
    if(i >= 5):
        break

print("\nFim do loop\n")


i = 0

carros = []
carro = input("Digite o nome do novo carro: ")

tam = len(carros)

while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

os.system('cls')
for x in carros:
    print(x)

print("\nFim do loop")