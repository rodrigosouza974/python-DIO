"""Em Python, variáveis e funções têm escopos que 
determinam onde essas variáveis podem ser acessadas e
 modificadas. Existem principalmente dois tipos de escopo: local e global.
"""
### Escopo Global

"""Variáveis definidas no nível mais externo de
 um script ou módulo têm escopo global. Elas podem 
 ser acessadas em qualquer lugar do código, incluindo 
 dentro de funções, desde que não sejam sobrescritas por variáveis locais.
"""
x = 10  # Variável global

def funcao():
    print(x)  # Acessa a variável global x

funcao()  # Saída: 10
print(x)  # Saída: 10

### Escopo Local

"""Variáveis definidas dentro de uma função têm escopo local.
 Elas só podem ser acessadas dentro da função onde foram definidas.
"""
#### Exemplo de Escopo Local
def funcao():
    y = 5  # Variável local
    print(y)  # Acessa a variável local y

funcao()  # Saída: 5
# print(y)  # Isso causará um erro, pois y não é acessível fora da função

### Modificando Variáveis Globais Dentro de Funções

"""Para modificar uma variável global dentro de uma 
função, você deve usar a palavra-chave `global`. Sem 
isso, qualquer atribuição a uma variável com o mesmo 
nome dentro da função criará uma nova variável local.
"""
#### Exemplo Usando `global`

x = 10  # Variável global

def funcao():
    global x
    x = 20  # Modifica a variável global x
    print(x)  # Saída: 20

funcao()
print(x)  # Saída: 20

### A Palavra-Chave `nonlocal`

"""Além de `global`, existe `nonlocal`, que permite
 modificar variáveis em um escopo de função aninhada 
 (enclosing scope). É útil para trabalhar com funções dentro de funções.
"""
#### Exemplo Usando `nonlocal`
def funcao_externa():
    x = 10  # Variável na função externa

    def funcao_interna():
        nonlocal x
        x = 20  # Modifica a variável da função externa
        print(x)  # Saída: 20

    funcao_interna()
    print(x)  # Saída: 20

funcao_externa()

### Resumo

"""- **Escopo Global**: Variáveis definidas fora de todas as funções, acessíveis de qualquer lugar do código.
- **Escopo Local**: Variáveis definidas dentro de uma função, acessíveis apenas dentro dessa função.
- **`global`**: Permite modificar variáveis globais dentro de funções.
- **`nonlocal`**: Permite modificar variáveis de um escopo de função aninhada.
"""
### Exemplos Práticos

#### 1. Escopo Global e Local
x = 100  # Variável global

def minha_funcao():
    y = 200  # Variável local
    print("Dentro da função, x:", x)  # Acessa variável global
    print("Dentro da função, y:", y)  # Acessa variável local

minha_funcao()
print("Fora da função, x:", x)  # Acessa variável global
# print("Fora da função, y:", y)  # Erro: y não é definida no escopo global

#### 2. Modificando Variável Global
x = 100

def minha_funcao():
    global x
    x = 200
    print("Dentro da função, x modificado para:", x)

minha_funcao()
print("Fora da função, x agora é:", x)  # Saída: Fora da função, x agora é: 200

#### 3. Usando `nonlocal`
def externa():
    x = 10

    def interna():
        nonlocal x
        x = 20
        print("Dentro da função interna, x:", x)

    interna()
    print("Dentro da função externa, x depois da modificação:", x)

externa()


"""Entender o escopo de variáveis é essencial para 
evitar bugs e garantir que seu código se comporte conforme esperado."""