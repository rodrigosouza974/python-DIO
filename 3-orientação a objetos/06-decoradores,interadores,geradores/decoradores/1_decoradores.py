"""Os decoradores são funções que modificam o comportamento de outras funções ou métodos. 
Decoradores internos (inner functions) podem se referir à prática de definir 
decoradores dentro de outras funções. Aqui está uma explicação de como eles 
funcionam e como você pode utilizá-los:
"""
### Definindo Decoradores

"""Um decorador é uma função que recebe outra função como argumento e retorna uma nova 
função que geralmente adiciona algum tipo de comportamento antes ou 
depois da função original.
"""
### Parte 1: Função Simples

"""Primeiro, vamos criar uma função simples que imprime uma mensagem.
"""
def diz_ola():
    print("Olá!")

"""Quando chamamos `diz_ola()`, a saída será:
Olá!
"""
### Parte 2: Decorador Simples

"""Agora, vamos criar um decorador simples que modifica o comportamento da função `diz_ola`.
"""
def meu_decorador(funcao):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        funcao()
        print("Algo está acontecendo depois que a função foi chamada.")
    return wrapper

"""Este decorador (`meu_decorador`) imprime uma mensagem antes e depois 
de chamar a função original.
"""

### Parte 3: Aplicando o Decorador

"""Vamos aplicar o decorador à função `diz_ola`.
"""
@meu_decorador
def diz_ola():
    print("Olá!")

"""Agora, quando chamamos `diz_ola()`, a saída será:
Algo está acontecendo antes da função ser chamada.
Olá!
Algo está acontecendo depois que a função foi chamada.
"""
### Parte 4: Decorador com Parâmetros

"""Vamos criar um decorador que aceita parâmetros. Este 
decorador repetirá a execução de uma função um número especificado de vezes.
"""
def repeticoes(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador

"""Neste decorador:

- `repeticoes(n)` cria um decorador que repetirá a execução `n` vezes.
- `decorador(funcao)` é o decorador que aceita a função a ser decorada.
- `wrapper(*args, **kwargs)` executa a função decorada `n` vezes."""

### Parte 5: Aplicando o Decorador com Parâmetros

"""Vamos aplicar o decorador com parâmetros à função `diz_bom_dia`.
"""
@repeticoes(3)
def diz_bom_dia():
    print("Bom dia!")

"""Quando chamamos `diz_bom_dia()`, a saída será:

Bom dia!
Bom dia!
Bom dia!
"""
### Parte 6: Decorador Definido Dentro de Outra Função

"""Vamos criar um exemplo onde o decorador é definido dentro de outra função.
"""
def cria_decorador_de_repeticoes(n):
    def decorador(funcao):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                funcao(*args, **kwargs)
        return wrapper
    return decorador

#Neste exemplo:

"""- `cria_decorador_de_repeticoes(n)` é uma função 
que cria um decorador que repetirá a execução `n` vezes.

Aplicamos este decorador a uma função:
"""
decorador_de_tres_repeticoes = cria_decorador_de_repeticoes(3)

@decorador_de_tres_repeticoes
def diz_boa_tarde():
    print("Boa tarde!")

"""Quando chamamos `diz_boa_tarde()`, a saída será:
Boa tarde!
Boa tarde!
Boa tarde!
"""

Isso acontece porque decoradores em Python são funções que recebem outra função como argumento, adicionam algum comportamento a essa função, e retornam uma nova função que inclui o comportamento adicional.

Vamos entender passo a passo o que está acontecendo no exemplo do decorador `meu_decorador`:

1. **Definição do Decorador**:
    ```python
    def meu_decorador(funcao):
        def wrapper():
            print("Algo está acontecendo antes da função ser chamada.")
            funcao()
            print("Algo está acontecendo depois que a função foi chamada.")
        return wrapper
    ```

    Aqui, `meu_decorador` é um decorador que recebe uma função (`funcao`) como argumento. Dentro dele, definimos uma nova função `wrapper`, que inclui o comportamento adicional de imprimir mensagens antes e depois de chamar a função original (`funcao`). No final, o `meu_decorador` retorna a função `wrapper`.

2. **Usando o Decorador**:
    ```python
    @meu_decorador
    def diz_ola():
        print("Olá!")
    ```

    Quando usamos o símbolo `@meu_decorador` acima da definição da função `diz_ola`, isso é equivalente a:
    ```python
    diz_ola = meu_decorador(diz_ola)
    ```

    Aqui, `diz_ola` é passado como argumento para `meu_decorador`, que retorna a função `wrapper`. Portanto, `diz_ola` agora se refere à função `wrapper`.

3. **Chamando a Função Decorada**:
    ```python
    diz_ola()
    ```

    Quando chamamos `diz_ola()`, na verdade estamos chamando a função `wrapper` que foi retornada pelo decorador. Isso resulta no seguinte comportamento:

    - Imprime "Algo está acontecendo antes da função ser chamada."
    - Chama a função original `diz_ola()`, que imprime "Olá!"
    - Imprime "Algo está acontecendo depois que a função foi chamada."

Portanto, o decorador modifica o comportamento da função `diz_ola` para incluir mensagens adicionais antes e depois da execução da função original.