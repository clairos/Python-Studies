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

vsql="SELECT * FROM tb_contatos WHERE N_IDCONTATO = 3"

def select(conexao, sql):
    c=conexao.cursor()
    c.execute(sql)
    result=c.fetchall()
    return result

res=select(vcon, vsql)

for r in res:
    print(r)