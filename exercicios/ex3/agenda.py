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
    print("1. Inserir Novo Registro")
    print("2. Deletar Registro ( por ID )")
    print("3. Atualizar Registro")
    print("4. Consultar todos os registros")
    print("5. Consultar Registro por ID")
    print("6. Consultar Registro por Nome")
    print("7. Sair")

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

def update(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
        print("Registro atualizado")

def selectID(conexao, sql):
    c=conexao.cursor()
    c.execute(sql)
    result=c.fetchall()

    print(result)

def selectName(conexao, sql):
    c=conexao.cursor()
    c.execute(sql)
    result=c.fetchall()

    print(result)

def select(conexao, sql):
    c=conexao.cursor()
    c.execute(sql)
    result=c.fetchall()

    for r in result:
        print(r)

opc = 0
vsql=""
while opc!=7:
    menu()
    opc=int(input("Digite uma opção: "))
    os.system('cls')

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
            opcup=0
            idcontato=int(input("Digite o ID do registro a ser atualizado: "))

            os.system('cls')
            print("O que deseja atualizar?")
            print("1. Nome")
            print("2. Telefone")
            print("3. Email\n")
            opcup=int(input())
            os.system('cls')

            match opcup:
                case 1:
                    nome=input("Digite o nome: ")
                    vsql="UPDATE tb_contatos SET T_NOMECONTATO = '" + nome + "' WHERE N_IDCONTATO = " + str(idcontato)
                case 2:
                    tel=input("Digite o telefone: ")
                    vsql="UPDATE tb_contatos SET T_TELEFONE = '" + tel + "' WHERE N_IDCONTATO = " + str(idcontato)
                case 3:
                    email=input("Digite o email: ")
                    vsql="UPDATE tb_contatos SET T_EMAILCONTATO = '" + email + "' WHERE N_IDCONTATO = " + str(idcontato)
                case _:
                    print("opção inválida.")

            update(vcon, vsql)
            os.system('pause')

        case 4:
            vsql="SELECT * FROM tb_contatos"
            select(vcon, vsql)
            os.system('pause')

        case 5:
            idcontato=input("Digite o ID: ")
            vsql="SELECT * FROM tb_contatos WHERE N_IDCONTATO = " + idcontato
            selectID(vcon, vsql)
            os.system('pause')

        case 6:
            nome=input("Digite o nome: ")
            vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO = '" + nome + "'"
            selectName(vcon, vsql)
            os.system('pause')
        
        case 7:
            os.system('cls')
            print("Programa finalizado.")

        case _:
            os.system('cls')
            print("Opção inválida")
            os.system('pause')