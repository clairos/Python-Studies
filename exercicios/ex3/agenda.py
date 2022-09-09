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
    print("2. Deletar Registro ( por ID )")
    print("3. Atualizar Registro")
    print("4. Consultar Registro por ID")
    print("5. Consultar Registro por Nome")
    print("6. Sair")

def insert(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Novo registro inserido.")

def delete(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)
    
    finally:
        print("Registro deletado.")

def update(): 
    print()

def selectID():
    print()

def selectName():
    print()


opc = 0
vsql=""
while opc!=6:
    menu()
    opc=int(input("Digite uma opção: "))

    match opc:
        case 1:
            nome=input("Digite o nome do novo registro: ")
            tel=input("Digite o telefone do novo registro: ")
            email=input("Digite o email do novo registro: ")
            vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONE, T_EMAILCONTATO) VALUES ('" + nome + "','" + tel + "','" + email + "')"
            insert(vcon, vsql)
            os.system('pause')

        case 2:
            idcontato=int(input("Digite o ID do registro a ser deletado: "))
            vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO = '" + idcontato + "'"
            delete(vcon, vsql)
            os.system('pause')

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