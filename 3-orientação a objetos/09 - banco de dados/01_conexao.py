import sqlite3
from pathlib import Path

ROOT_PATH =Path(__file__).parent

#cria o banco
conexao = sqlite3.connect(ROOT_PATH / "meubanco.sqlite")
cursor =conexao.cursor()

def criar_tabela(conexao,cursor):
    #cria as tabelas
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    conexao.commit()

def inserir_registro(conexao,cursor, nome, email):    
    data =(nome,email)
    cursor.execute("INSERT INTO clientes(nome,email) VALUES (?,?);",data) #insere dados na tabela
    conexao.commit()

def atualizar_registro(conexao,cursor, nome, email, id):
    data =(nome,email,id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;",data)
    conexao.commit()

def excluir_registro(conexao,cursor, id):
    data =(id)
    cursor.execute("DELETE FROM clientes WHERE id = ?;",data)
    conexao.commit()

#atualizar_registro(conexao,cursor,"Rodrigo souza", "rodrigosouza@hotmail.com",1)
excluir_registro(conexao,cursor,1)

