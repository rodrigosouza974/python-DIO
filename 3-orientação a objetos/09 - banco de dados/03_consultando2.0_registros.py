#utilizando ROW FACTORY

import sqlite3
from pathlib import Path

ROOT_PATH =Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meubanco.sqlite")
cursor =conexao.cursor()

def recupera_cliente (cursor, id):  
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id =?",(id,)) 
    return cursor.fetchone()

def listar_clientes(cursor):
    #return cursor.execute("SELECT * FROM clientes")
   return cursor.execute("SELECT * FROM clientes ORDER BY id DESC ;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)
    

cliente = recupera_cliente(cursor,4)
print(dict(cliente))
##ou
print(cliente['id'],cliente['nome'],cliente['email'])