### Argumentos Somente de Palavra-chave (Keyword-Only Arguments)

No Python, você pode definir funções que recebem argumentos de diferentes maneiras: por posição, por palavra-chave, ou ambos. Argumentos "somente de palavra-chave" são argumentos que devem ser passados para a função usando seu nome, não podem ser passados pela posição.

Vamos detalhar como isso funciona e por que é útil.

#### O Problema

Quando você define uma função em Python, você geralmente pode passar argumentos de duas maneiras:

1. **Posicionais**: A ordem em que você passa os argumentos importa.
    ```python
    def func(a, b):
        return a + b

    func(1, 2)  # a=1, b=2
    ```

2. **Palavra-chave**: Você pode nomear os argumentos ao chamá-los.
    ```python
    def func(a, b):
        return a + b

    func(a=1, b=2)  # a=1, b=2
    ```

Às vezes, você quer garantir que certos argumentos sejam passados apenas pelo nome para evitar confusão ou erros. Por exemplo, se você tiver muitos argumentos, pode ser difícil lembrar a ordem correta deles. É aqui que os argumentos somente de palavra-chave entram.

#### A Solução: Argumentos Somente de Palavra-chave

Os argumentos somente de palavra-chave são definidos de forma que você **deve** passar esses argumentos pelo nome, não pela posição. Isso é feito usando um asterisco (`*`) na definição da função.

#### Como Definir

Vamos ver um exemplo simples:

```python
def func(a, b, *, c):
    return a + b + c
```

Neste exemplo, `a` e `b` são argumentos posicionais, mas `c` é um argumento somente de palavra-chave. Isso significa que você **deve** passar `c` usando seu nome ao chamar a função:

```python
func(1, 2, c=3)  # Correto
```

Se você tentar passar `c` pela posição, o Python levantará um erro:

```python
func(1, 2, 3)  # TypeError: func() takes 2 positional arguments but 3 were given
```

#### Exemplo Prático

Vamos considerar uma função que lida com arquivos, onde você pode querer especificar o modo de abertura do arquivo de forma clara:

```python
def open_file(filename, *, mode='r'):
    with open(filename, mode) as file:
        return file.read()
```

Aqui, `filename` é um argumento posicional, mas `mode` é um argumento somente de palavra-chave. Isso ajuda a evitar erros acidentais ao passar o modo de abertura:

```python
open_file('example.txt', mode='w')  # Correto
open_file('example.txt', 'w')  # TypeError: open_file() takes 1 positional argument but 2 were given
```

#### Benefícios

1. **Clareza**: Força o uso de nomes de argumentos, tornando o código mais legível e claro.
2. **Segurança**: Evita erros comuns que podem ocorrer ao passar muitos argumentos posicionais na ordem errada.
3. **Flexibilidade**: Permite adicionar novos argumentos à função no futuro sem quebrar o código existente que chama a função.

#### Resumo

Os argumentos somente de palavra-chave são uma ferramenta poderosa no Python para criar APIs de funções mais claras e robustas. Eles garantem que certos argumentos sejam passados de maneira explícita, melhorando a legibilidade e reduzindo a chance de erros. Ao definir uma função, você pode usar o asterisco (`*`) para indicar que todos os argumentos seguintes devem ser passados por nome.