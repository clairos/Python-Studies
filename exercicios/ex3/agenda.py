import os
import sqlite3 
from sqlite3 import Error 

def dbConnection(): # funcao para fazer a conexao com o banco de dados
    path="C:\\Users\\clara.brusa\\Desktop\Python\\banco\\agenda.db"
    con=None # connection

    try:
        con=sqlite3.connect(path)

    except Error as ex:
        print(ex)
    
    return con

vcon=dbConnection()

def menu():
    os.system('cls')
    print("1. Inserir Novo Registros")
    print("2. Deletar Registro")
    print("3. Atualizar Registro")
    print("4. Consultar Registro por ID")
    print("5. Consultar Registro por Nome")
    print("6. Sair")

def insert():
    print()

def delete():
    print()

def update(): 
    print()

def selectID():
    print()

def selectName():
    print()


opc = 0
while opc!=6:
    menu()
    opc=int(input("Digite uma opção: "))

    match opc:
        case 1:
            insert()
        case 2:
            delete()
        case 3:
            update()
        case 4:
            selectID()
        case 5:
            selectName()
        case 6:
            os.system('cls')
            print("Programa finalizado.")
        case _:
            os.system('cls')
            print("Opção inválida")
            os.system('pause')