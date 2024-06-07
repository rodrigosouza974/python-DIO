### Argumentos Somente Posicionais (Positional-Only Arguments)

No Python, assim como podemos ter argumentos que só podem ser passados por palavra-chave, também podemos ter argumentos que só podem ser passados por posição. Argumentos somente posicionais são úteis quando queremos que certos parâmetros sejam sempre fornecidos na ordem correta, sem a possibilidade de serem confundidos com argumentos de palavra-chave.

#### O Problema

Às vezes, ao projetar funções, queremos garantir que determinados argumentos sejam sempre passados em uma ordem específica. Por exemplo, funções matemáticas simples ou operações básicas onde a ordem dos argumentos é crucial.

#### A Solução: Argumentos Somente Posicionais

A partir do Python 3.8, podemos definir argumentos que só podem ser passados por posição usando uma barra (`/`) na definição da função. A barra indica que todos os argumentos antes dela são somente posicionais.

#### Como Definir

Vamos ver um exemplo simples:

```python
def func(a, b, /, c, d):
    return a + b + c + d
```

Neste exemplo, `a` e `b` são argumentos somente posicionais, enquanto `c` e `d` podem ser passados tanto por posição quanto por palavra-chave.

#### Exemplo Prático

Imagine que você está criando uma função para adicionar dois números. Você quer que esses números sejam sempre passados por posição:

```python
def add(x, y, /):
    return x + y
```

Aqui, `x` e `y` são argumentos somente posicionais. Você deve passá-los pela posição ao chamar a função:

```python
add(1, 2)  # Correto
```

Se você tentar passar `x` ou `y` como argumentos de palavra-chave, o Python levantará um erro:

```python
add(x=1, y=2)  # TypeError: add() got some positional-only arguments passed as keyword arguments: 'x, y'
```

#### Combinação com Argumentos Somente de Palavra-chave

Você pode combinar argumentos somente posicionais e somente de palavra-chave na mesma função para controlar exatamente como os argumentos podem ser passados:

```python
def complex_func(a, b, /, c, *, d):
    return a + b + c + d
```

Neste exemplo:
- `a` e `b` são somente posicionais.
- `c` pode ser passado por posição ou por palavra-chave.
- `d` é somente de palavra-chave.

Chamar esta função corretamente seria:

```python
complex_func(1, 2, 3, d=4)  # Correto
complex_func(1, 2, c=3, d=4)  # Correto
```

Chamar esta função de maneira incorreta levantará um erro:

```python
complex_func(1, 2, 3, 4)  # TypeError: complex_func() takes 3 positional arguments but 4 were given
complex_func(a=1, b=2, c=3, d=4)  # TypeError: complex_func() got some positional-only arguments passed as keyword arguments: 'a, b'
```

#### Benefícios

1. **Clareza**: Força o uso de uma ordem específica para certos argumentos, tornando o código mais claro em termos de como a função deve ser chamada.
2. **Segurança**: Evita a passagem de argumentos na ordem errada, o que pode levar a resultados inesperados.
3. **Simplicidade**: Para funções onde a ordem dos argumentos é intuitiva e clara, o uso de argumentos somente posicionais simplifica a chamada da função.

#### Resumo

Argumentos somente posicionais são uma adição útil ao Python para criar APIs de funções mais claras e seguras. Eles garantem que certos argumentos sejam passados na ordem correta, evitando confusões e erros. Você pode definir argumentos somente posicionais usando a barra (`/`) na definição da função, e essa funcionalidade pode ser combinada com argumentos somente de palavra-chave para um controle completo sobre como os argumentos são passados para a função.