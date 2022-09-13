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

vsql = "UPDATE tb_contatos SET T_NOMECONTATO = 'Ana' WHERE N_IDCONTATO = 4"

def update(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)
        
    finally:
        print("Registro atualizado")

update(vcon, vsql)