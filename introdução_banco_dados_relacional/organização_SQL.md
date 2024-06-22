DQL (Data Query Language) é uma sublinguagem do SQL (Structured Query Language) usada para realizar consultas e recuperar dados de um banco de dados relacional. O comando principal da DQL é o `SELECT`, que permite selecionar dados de uma ou mais tabelas. Além da DQL, outras sublinguagens importantes do SQL são DDL (Data Definition Language), DML (Data Manipulation Language) e DCL (Data Control Language).

### Exemplos de Comandos SQL

#### Data Query Language (DQL)
A DQL é utilizada para consultar dados no banco de dados. O comando principal é `SELECT`.

##### Seleção Simples
```sql
SELECT * FROM Cliente;
```
Este comando seleciona todas as colunas de todas as linhas da tabela `Cliente`.

##### Seleção Específica
```sql
SELECT Nome, Email FROM Cliente WHERE ID = 1;
```
Este comando seleciona as colunas `Nome` e `Email` da tabela `Cliente` onde o `ID` é igual a 1.

##### Ordenação de Resultados
```sql
SELECT * FROM Livro ORDER BY Título;
```
Este comando seleciona todas as colunas da tabela `Livro` e ordena os resultados pelo título.

##### Junção de Tabelas (JOIN)
```sql
SELECT Pedido.ID, Cliente.Nome, Livro.Título, PedidoLivro.Quantidade
FROM Pedido
JOIN Cliente ON Pedido.ClienteID = Cliente.ID
JOIN PedidoLivro ON Pedido.ID = PedidoLivro.PedidoID
JOIN Livro ON PedidoLivro.LivroID = Livro.ID;
```
Este comando seleciona dados de várias tabelas relacionadas e retorna o ID do pedido, nome do cliente, título do livro e quantidade de cada item pedido.

### Data Definition Language (DDL)
A DDL é usada para definir e modificar a estrutura do banco de dados.

##### Criação de Tabela
```sql
CREATE TABLE Autor (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100)
);
```
Este comando cria uma tabela chamada `Autor` com colunas `ID` e `Nome`.

##### Alteração de Tabela
```sql
ALTER TABLE Livro ADD COLUMN Publicacao DATE;
```
Este comando adiciona uma nova coluna `Publicacao` à tabela `Livro`.

##### Exclusão de Tabela
```sql
DROP TABLE Autor;
```
Este comando exclui a tabela `Autor`.

### Data Manipulation Language (DML)
A DML é usada para manipular os dados dentro das tabelas.

##### Inserção de Dados
```sql
INSERT INTO Cliente (ID, Nome, Email, Endereço) VALUES (2, 'Maria Oliveira', 'maria.oliveira@example.com', 'Rua B, 456');
```
Este comando insere um novo registro na tabela `Cliente`.

##### Atualização de Dados
```sql
UPDATE Livro SET Preço = 29.90 WHERE ID = 1;
```
Este comando atualiza o preço do livro com `ID` igual a 1.

##### Exclusão de Dados
```sql
DELETE FROM Cliente WHERE ID = 2;
```
Este comando exclui o registro da tabela `Cliente` onde o `ID` é igual a 2.

### Data Control Language (DCL)
A DCL é usada para controlar o acesso aos dados no banco de dados.

##### Concessão de Permissões
```sql
GRANT SELECT, INSERT ON Livro TO usuario;
```
Este comando concede permissões de seleção e inserção na tabela `Livro` ao usuário `usuario`.

##### Revogação de Permissões
```sql
REVOKE INSERT ON Livro FROM usuario;
```
Este comando revoga a permissão de inserção na tabela `Livro` do usuário `usuario`.

### Exemplos Práticos

#### Criar e Consultar Tabelas

1. **Criação de Tabelas**
```sql
CREATE TABLE Cliente (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    Endereço VARCHAR(200)
);

CREATE TABLE Livro (
    ID INT PRIMARY KEY,
    Título VARCHAR(100),
    Autor VARCHAR(100),
    Preço DECIMAL(10, 2)
);

CREATE TABLE Pedido (
    ID INT PRIMARY KEY,
    Data DATE,
    ClienteID INT,
    FOREIGN KEY (ClienteID) REFERENCES Cliente(ID)
);

CREATE TABLE PedidoLivro (
    PedidoID INT,
    LivroID INT,
    Quantidade INT,
    PRIMARY KEY (PedidoID, LivroID),
    FOREIGN KEY (PedidoID) REFERENCES Pedido(ID),
    FOREIGN KEY (LivroID) REFERENCES Livro(ID)
);
```

2. **Inserção de Dados**
```sql
INSERT INTO Cliente (ID, Nome, Email, Endereço) VALUES (1, 'João Silva', 'joao.silva@example.com', 'Rua A, 123');
INSERT INTO Livro (ID, Título, Autor, Preço) VALUES (1, 'SQL para Iniciantes', 'Carlos Souza', 39.90);
INSERT INTO Pedido (ID, Data, ClienteID) VALUES (1, '2024-06-21', 1);
INSERT INTO PedidoLivro (PedidoID, LivroID, Quantidade) VALUES (1, 1, 2);
```

3. **Consultas**
```sql
-- Selecionar todos os clientes
SELECT * FROM Cliente;

-- Selecionar todos os livros
SELECT * FROM Livro;

-- Selecionar pedidos com detalhes dos livros e clientes
SELECT Pedido.ID, Cliente.Nome, Livro.Título, PedidoLivro.Quantidade
FROM Pedido
JOIN Cliente ON Pedido.ClienteID = Cliente.ID
JOIN PedidoLivro ON Pedido.ID = PedidoLivro.PedidoID
JOIN Livro ON PedidoLivro.LivroID = Livro.ID;
```

Esses exemplos cobrem as principais operações e comandos necessários para a organização e gestão de um banco de dados relacional, utilizando as sublinguagens DQL, DDL, DML e DCL.