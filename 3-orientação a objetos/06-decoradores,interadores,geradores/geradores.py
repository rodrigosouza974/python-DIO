Um gerador em Python é uma função que permite iterar sobre um conjunto de valores, um de cada vez, sem armazenar todos os valores na memória ao mesmo tempo. Em vez disso, ele gera os valores sob demanda, o que é útil para trabalhar com grandes volumes de dados ou sequências infinitas.

Os geradores são definidos como funções normais, mas utilizam a palavra-chave `yield` em vez de `return`. Quando uma função geradora é chamada, ela retorna um objeto gerador sem executar o corpo da função imediatamente. Cada vez que a função `next()` é chamada no gerador, a função executa até encontrar uma instrução `yield`, que retorna o valor indicado e pausa a execução da função. A próxima chamada para `next()` retoma a execução a partir do ponto onde parou.

Aqui estão alguns exemplos de uso de geradores em Python:

### Exemplo 1: Contador Simples

```python
def contador(n):
    i = 0
    while i < n:
        yield i
        i += 1

# Usando o gerador
for num in contador(5):
    print(num)
```

### Exemplo 2: Sequência Fibonacci

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usando o gerador
fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### Exemplo 3: Ler um arquivo linha por linha

```python
def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usando o gerador
for linha in ler_arquivo('meuarquivo.txt'):
    print(linha)
```

### Exemplo 4: Números pares até um limite

```python
def numeros_pares(limite):
    for num in range(limite):
        if num % 2 == 0:
            yield num

# Usando o gerador
for par in numeros_pares(10):
    print(par)
```

Esses exemplos demonstram como os geradores podem ser usados para produzir sequências de valores de maneira eficiente, sem a necessidade de carregar todos os dados na memória ao mesmo tempo.