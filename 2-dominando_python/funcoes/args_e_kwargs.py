"""Vamos explorar como usar `*args` e `**kwargs` em funções 
Python. Esses são mecanismos poderosos que permitem passar 
um número variável de argumentos para uma função.
"""
### `*args`
"""`*args` permite que você passe um número variável 
de argumentos posicionais para uma função.
"""
def soma(*args):
    # args é uma tupla contendo todos os argumentos posicionais passados
    return sum(args)

# Chamando a função com diferentes números de argumentos
print(soma(1, 2, 3))  # Saída: 6
print(soma(4, 5))     # Saída: 9
print(soma(10))       # Saída: 10

### `**kwargs`
"""`**kwargs` permite que você passe um número variável
 de argumentos nomeados (chave-valor) para uma função.
"""
def exibir_informacoes(**kwargs):
    # kwargs é um dicionário contendo todos os argumentos nomeados passados
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes argumentos nomeados
exibir_informacoes(nome="Alice", idade=30, cidade="São Paulo")
# Saída:
# nome: Alice
# idade: 30
# cidade: São Paulo

exibir_informacoes(produto="Notebook", preco=1500)
# Saída:
# produto: Notebook
# preco: 1500

### Usando `*args` e `**kwargs` Juntos
"""Você pode usar `*args` e `**kwargs` juntos na 
definição de uma função. `*args` deve ser listado
 antes de `**kwargs`.
"""
def misturar(argumento_fixo, *args, **kwargs):
    print("Argumento fixo:", argumento_fixo)
    print("args:", args)
    print("kwargs:", kwargs)

# Chamando a função
misturar(1, 2, 3, 4, nome="Alice", idade=30)
# Saída:
# Argumento fixo: 1
# args: (2, 3, 4)
# kwargs: {'nome': 'Alice', 'idade': 30}


### Exemplos Práticos
#### 1. Função para Calcular Média com `*args`
def calcular_media(*args):
    total = sum(args)
    quantidade = len(args)
    return total / quantidade if quantidade != 0 else 0

# Chamando a função
print(calcular_media(1, 2, 3, 4, 5))  # Saída: 3.0
print(calcular_media(10, 20))         # Saída: 15.0
print(calcular_media())               # Saída: 0

#### 2. Função para Exibir Detalhes do Produto com `**kwargs`
def exibir_detalhes_produto(**kwargs):
    print("Detalhes do Produto:")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

# Chamando a função
exibir_detalhes_produto(nome="Camiseta", preco=29.90, estoque=100)
# Saída:
# Detalhes do Produto:
# nome: Camiseta
# preco: 29.9
# estoque: 100

### Conclusão
"""usar `*args` e `**kwargs` nas funções Python permite
que você crie funções mais flexíveis e reutilizáveis.
`*args` é útil quando você não sabe de antemão quantos
argumentos posicionais serão passados para a função, 
enquanto `**kwargs` é útil quando você não sabe quantos
argumentos nomeados serão passados.

Esses mecanismos são amplamente utilizados em bibliotecas
Python e em código de produção para lidar com diferentes tipos 
e quantidades de argumentos de maneira elegante e eficaz.
"""