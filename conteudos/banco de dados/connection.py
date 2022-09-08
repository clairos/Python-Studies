import sqlite3
from sqlite3 import Error

def dbConnection(): # funcao para fazer a conexao com o banco de dados
    path="C:\\Users\\clara.brusa\\Desktop\Python\\banco\\agenda.db"
    con=None # connection

    try:
        con=sqlite3.connect(path)
        print("Conectado")

    except Error as ex:
        print(ex)
    
    return con

vcon=dbConnection()

# criar tabela:
# OBS: aspas triplas servem para criar string com varias linhas
vsql="""CREATE TABLE tb_contatos( 
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)
        );"""

def createTable(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")

    except Error as ex:
        print(ex)

createTable(vcon, vsql)

vcon.close()