Claro, vamos falar sobre decoradores em Python em português. Os decoradores são funções que modificam o comportamento de outras funções ou métodos. Decoradores internos (inner functions) podem se referir à prática de definir decoradores dentro de outras funções. Aqui está uma explicação de como eles funcionam e como você pode utilizá-los:

### Definindo Decoradores

Um decorador é uma função que recebe outra função como argumento e retorna uma nova 
função que geralmente adiciona algum tipo de comportamento antes ou depois da função original.

### Parte 1: Função Simples

Primeiro, vamos criar uma função simples que imprime uma mensagem.

```python
def diz_ola():
    print("Olá!")
```

Quando chamamos `diz_ola()`, a saída será:

```
Olá!
```

### Parte 2: Decorador Simples

Agora, vamos criar um decorador simples que modifica o comportamento da função `diz_ola`.

```python
def meu_decorador(funcao):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        funcao()
        print("Algo está acontecendo depois que a função foi chamada.")
    return wrapper
```

Este decorador (`meu_decorador`) imprime uma mensagem antes e depois de chamar a função original.

### Parte 3: Aplicando o Decorador

Vamos aplicar o decorador à função `diz_ola`.

```python
@meu_decorador
def diz_ola():
    print("Olá!")
```

Agora, quando chamamos `diz_ola()`, a saída será:

```
Algo está acontecendo antes da função ser chamada.
Olá!
Algo está acontecendo depois que a função foi chamada.
```

### Parte 4: Decorador com Parâmetros

Vamos criar um decorador que aceita parâmetros. Este decorador repetirá a execução de uma função um número especificado de vezes.

```python
def repeticoes(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador
```

Neste decorador:

- `repeticoes(n)` cria um decorador que repetirá a execução `n` vezes.
- `decorador(funcao)` é o decorador que aceita a função a ser decorada.
- `wrapper(*args, **kwargs)` executa a função decorada `n` vezes.

### Parte 5: Aplicando o Decorador com Parâmetros

Vamos aplicar o decorador com parâmetros à função `diz_bom_dia`.

```python
@repeticoes(3)
def diz_bom_dia():
    print("Bom dia!")
```

Quando chamamos `diz_bom_dia()`, a saída será:

```
Bom dia!
Bom dia!
Bom dia!
```

### Parte 6: Decorador Definido Dentro de Outra Função

Vamos criar um exemplo onde o decorador é definido dentro de outra função.

```python
def cria_decorador_de_repeticoes(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador
```

Neste exemplo:

- `cria_decorador_de_repeticoes(n)` é uma função que cria um decorador que repetirá a execução `n` vezes.

Aplicamos este decorador a uma função:

```python
decorador_de_tres_repeticoes = cria_decorador_de_repeticoes(3)

@decorador_de_tres_repeticoes
def diz_boa_tarde():
    print("Boa tarde!")
```

Quando chamamos `diz_boa_tarde()`, a saída será:

```
Boa tarde!
Boa tarde!
Boa tarde!
```