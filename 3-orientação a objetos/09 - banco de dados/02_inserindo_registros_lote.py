import sqlite3
from pathlib import Path

ROOT_PATH =Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meubanco.sqlite")
cursor =conexao.cursor()

def inserir_muitos(conexao,cursor, dados):    
    cursor.executemany("INSERT INTO clientes(nome,email) VALUES (?,?);",dados) 
    #insere dados em massa na tabela
    conexao.commit()

dados =[
    ('rodrigo','rodrigogmail.com'),
    ('ana','anagmail.com'),
    ('luiz','luizgmail.com'),
    ('carlos','carlosgmail.com'),
    ('maria','mariagmail.com'),
    ('diogo','diogogmail.com'),
]
inserir_muitos(conexao,cursor,dados)