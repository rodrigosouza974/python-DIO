Manipular arquivos em Python é uma tarefa comum e relativamente simples. Você pode ler, escrever, e até mesmo modificar arquivos de várias maneiras. Aqui estão alguns exemplos básicos de como manipular arquivos em Python.

### Abrir e Fechar Arquivos

A maneira mais básica de manipular arquivos em Python é usando a função `open()` para abrir um arquivo e a função `close()` para fechá-lo.

```python
# Abrindo um arquivo para leitura
file = open('exemplo.txt', 'r')
# Lendo o conteúdo do arquivo
conteudo = file.read()
print(conteudo)
# Fechando o arquivo
file.close()
```

### Usando Context Manager

Usar um `with` statement é uma prática recomendada, pois garante que o arquivo será fechado corretamente após a execução do bloco de código.

```python
with open('exemplo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)
# O arquivo é fechado automaticamente aqui
```

### Escrever em Arquivos

Para escrever em um arquivo, você pode abrir o arquivo no modo de escrita (`'w'`), de adição (`'a'`), ou de atualização (`'r+'`).

```python
# Abrindo um arquivo para escrita
with open('exemplo.txt', 'w') as file:
    file.write('Olá, mundo!')
```

### Ler Linhas de um Arquivo

Você pode ler o arquivo linha por linha usando um loop.

```python
with open('exemplo.txt', 'r') as file:
    for linha in file:
        print(linha, end='')
```

### Modos de Abertura de Arquivo

- `'r'`: Leitura (padrão).
- `'w'`: Escrita (cria um novo arquivo ou substitui um existente).
- `'a'`: Adição (adiciona ao final do arquivo).
- `'b'`: Binário (usado com outros modos, por exemplo, `'rb'` ou `'wb'`).
- `'+'`: Atualização (leitura e escrita).

### Manipular Arquivos CSV

Para manipular arquivos CSV, a biblioteca `csv` é muito útil.

```python
import csv

# Escrever em um arquivo CSV
with open('dados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nome', 'Idade'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

# Ler de um arquivo CSV
with open('dados.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

Esses são alguns exemplos básicos de como manipular arquivos em Python. Dependendo da necessidade, você pode usar bibliotecas adicionais como `pandas` para manipulação de dados mais complexa em arquivos CSV, Excel, entre outros.