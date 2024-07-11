import sqlite3
from pathlib import Path

ROOT_PATH =Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meubanco.sqlite")
cursor =conexao.cursor()

def recupera_cliente (cursor, id):    
    cursor.execute("SELECT * FROM clientes WHERE id =?",(id,)) 
    return cursor.fetchone()

def listar_clientes(cursor):
    #return cursor.execute("SELECT * FROM clientes")
   return cursor.execute("SELECT * FROM clientes ORDER BY id DESC ;")


cliente = recupera_cliente(cursor,4)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)