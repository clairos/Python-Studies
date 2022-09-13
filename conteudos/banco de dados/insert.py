import sqlite3
from sqlite3 import Error

def dbConnection(): # funcao para fazer a conexao com o banco de dados
    path = "C:\\Users\\clara.brusa\\Desktop\Python\\banco\\agenda.db"
    con = None # connection

    try:
        con = sqlite3.connect(path)

    except Error as ex:
        print(ex)
    
    return con

vcon = dbConnection()

nome = input("Digite o nome: ")
tel = input("Digite o telefone: ")
email = input("Digite o email: ")

vsql = "INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONE, T_EMAILCONTATO) VALUES ('" + nome + "','" + tel + "','" + email + "')"

def insert(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido")

    except Error as ex:
        print(ex)

insert(vcon, vsql)