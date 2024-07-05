Escrever em arquivos em Python pode ser feito de várias maneiras, dependendo do que você precisa fazer. Aqui estão alguns exemplos comuns de escrita em arquivos.

### Escrever Texto em Arquivos

1. **Escrever uma string em um arquivo:**

```python
# Abrir o arquivo no modo de escrita (isso cria um novo arquivo ou sobrescreve o existente)
with open('exemplo.txt', 'w') as file:
    file.write('Olá, mundo!')
```

2. **Adicionar texto a um arquivo existente:**

```python
# Abrir o arquivo no modo de adição (isso adiciona ao final do arquivo)
with open('exemplo.txt', 'a') as file:
    file.write('\nEsta é uma nova linha.')
```

3. **Escrever múltiplas linhas em um arquivo:**

```python
linhas = [
    'Primeira linha.\n',
    'Segunda linha.\n',
    'Terceira linha.\n'
]

with open('exemplo.txt', 'w') as file:
    file.writelines(linhas)
```

### Escrever Dados Estruturados em Arquivos CSV

1. **Usar a biblioteca `csv` para escrever em um arquivo CSV:**

```python
import csv

dados = [
    ['Nome', 'Idade'],
    ['Alice', 30],
    ['Bob', 25],
    ['Charlie', 35]
]

with open('dados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dados)
```

2. **Escrever um dicionário em um arquivo CSV:**

```python
import csv

dados = [
    {'Nome': 'Alice', 'Idade': 30},
    {'Nome': 'Bob', 'Idade': 25},
    {'Nome': 'Charlie', 'Idade': 35}
]

with open('dados.csv', 'w', newline='') as csvfile:
    fieldnames = ['Nome', 'Idade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(dados)
```

### Escrever em Arquivos Binários

1. **Escrever bytes em um arquivo binário:**

```python
# Escrevendo dados binários em um arquivo
with open('exemplo.bin', 'wb') as file:
    data = b'Hello, world!'  # Dados binários
    file.write(data)
```

### Exemplo Completo de Manipulação de Arquivos

Aqui está um exemplo completo que cobre a leitura e escrita de arquivos de texto e CSV:

```python
# Escrevendo texto em um arquivo
with open('exemplo.txt', 'w') as file:
    file.write('Primeira linha de texto.\n')
    file.write('Segunda linha de texto.\n')

# Lendo e adicionando a um arquivo de texto
with open('exemplo.txt', 'a') as file:
    file.write('Adicionando uma terceira linha.\n')

with open('exemplo.txt', 'r') as file:
    conteudo = file.read()
    print('Conteúdo do arquivo de texto:')
    print(conteudo)

# Escrevendo dados em um arquivo CSV
import csv

dados = [
    ['Nome', 'Idade'],
    ['Alice', 30],
    ['Bob', 25]
]

with open('dados.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dados)

# Lendo dados de um arquivo CSV
with open('dados.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print('Conteúdo do arquivo CSV:')
    for row in reader:
        print(row)
```

Esses exemplos cobrem as operações básicas de escrita em arquivos de texto, CSV e binários em Python. Se precisar de algo mais específico ou avançado, sinta-se à vontade para perguntar!