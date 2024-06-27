Claro! Vamos criar um exemplo de um gerador que simula a leitura de registros de um banco de dados. Suponha que temos uma tabela chamada `clientes` em um banco de dados e queremos iterar sobre todos os registros dessa tabela sem carregar todos os dados na memória de uma vez.

Vamos usar o módulo `sqlite3` do Python para criar um banco de dados SQLite e, em seguida, criar um gerador para iterar sobre os registros.

### Passo 1: Criar o Banco de Dados e Inserir Dados

```python
import sqlite3

# Conectar ao banco de dados (ou criar um novo banco)
conexao = sqlite3.connect('meubanco.db')
cursor = conexao.cursor()

# Criar a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT
    )
''')

# Inserir alguns dados
clientes = [
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com'),
    ('Pedro', 'pedro@example.com')
]

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)

# Salvar as mudanças e fechar a conexão
conexao.commit()
conexao.close()
```

### Passo 2: Criar o Gerador para Iterar sobre os Registros

```python
import sqlite3

def ler_clientes(db_path):
    conexao = sqlite3.connect(db_path)
    cursor = conexao.cursor()
    
    cursor.execute('SELECT id, nome, email FROM clientes')
    while True:
        registro = cursor.fetchone()
        if registro is None:
            break
        yield registro
    
    conexao.close()

# Usando o gerador
for cliente in ler_clientes('meubanco.db'):
    print(cliente)
```

### Explicação

1. **Criar o Banco de Dados e Inserir Dados**: Primeiro, criamos uma conexão com o banco de dados e uma tabela `clientes`, onde inserimos alguns registros de exemplo.

2. **Criar o Gerador**: A função `ler_clientes` é um gerador que se conecta ao banco de dados, executa uma consulta para selecionar todos os registros da tabela `clientes` e, em seguida, usa um loop para buscar e retornar um registro por vez usando `yield`. O loop continua até que não haja mais registros (`fetchone` retorna `None` quando não há mais registros).

3. **Usar o Gerador**: Finalmente, usamos o gerador em um loop `for` para iterar sobre todos os registros da tabela `clientes` e imprimir cada um deles.

Este exemplo demonstra como você pode usar geradores para iterar eficientemente sobre registros de um banco de dados, lendo um registro por vez sem carregar todos os dados na memória.