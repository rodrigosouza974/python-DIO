"""Métodos de classe e métodos estáticos em Python são utilizados para diferentes 
propósitos e possuem características distintas. Vamos detalhar as diferenças 
entre eles e dar exemplos de cada um.
"""
### Métodos de Classe
"""
Métodos de classe são métodos que são vinculados à classe e não à instância da classe.
Eles têm acesso à classe através de um parâmetro especial `cls`. Você pode definir um 
método de classe usando o decorador `@classmethod`."""

"""**Características:**
- Recebem um parâmetro implícito `cls` que representa a classe.
- Podem acessar e modificar o estado da classe que é compartilhado entre todas as instâncias.

Um método de classe recebe um parâmetro implícito que é a própria classe (cls). 
Ele pode acessar ou modificar o estado da classe, mas não o estado da instância. 
Você usa @classmethod quando o método precisa acessar ou modificar atributos da 
classe ou quando você precisa trabalhar com a classe em si (por exemplo, criando 
instâncias de subclasses).

Quando usar:

Quando o método precisa acessar ou modificar atributos da classe.
Quando o método precisa trabalhar com a própria classe, por exemplo, para 
criar instâncias da classe ou de subclasses.

Resumo
Use @staticmethod quando você tem um método que não precisa acessar ou
 modificar o estado da classe ou da instância.
Use @classmethod quando você tem um método que precisa acessar ou modificar
 o estado da classe ou quando você precisa trabalhar com a classe em si.
**Exemplo:**"""
class MinhaClasse:
    contador = 0

    def __init__(self):
        MinhaClasse.contador += 1

    @classmethod
    def obter_contador(cls):
        return cls.contador

# Criando instâncias da classe
instancia1 = MinhaClasse()
instancia2 = MinhaClasse()

# Usando o método de classe
print(MinhaClasse.obter_contador())  # Saída: 2


### Métodos Estáticos
Métodos estáticos são métodos que não recebem implicitamente nenhum argumento da instância ou da classe. Eles são basicamente funções que são definidas dentro de uma classe por motivos de organização. Você pode definir um método estático usando o decorador `@staticmethod`.

**Características:**
- Não recebem o parâmetro `self` ou `cls`.
- Não podem modificar o estado da instância ou da classe.
- Úteis para funções que têm uma relação lógica com a classe, mas não precisam acessar ou modificar seus atributos.

Um método estático não tem acesso a instâncias da classe (self) nem à própria classe (cls). Ele é como uma função comum, mas está associada à classe e não ao objeto da classe. Você usa @staticmethod quando a função que você está definindo não precisa acessar nem modificar o estado da classe ou da instância.

Quando usar:

Quando o método não precisa acessar ou modificar atributos da classe ou da instância.
Quando o método é uma função utilitária que logicamente pertence à classe, mas não depende de nenhuma instância específica.

**Exemplo:**
```python
class Utilidades:
    
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b

# Usando métodos estáticos
print(Utilidades.somar(5, 3))       # Saída: 8
print(Utilidades.subtrair(10, 4))   # Saída: 6
```

### Comparação

- **Métodos de Classe**:
  - Recebem `cls` como primeiro argumento.
  - Podem acessar e modificar atributos de classe.
  - Úteis quando você precisa trabalhar com a classe em vez de com instâncias específicas.

- **Métodos Estáticos**:
  - Não recebem `self` ou `cls`.
  - Não podem acessar ou modificar atributos de classe ou de instância.
  - Úteis para funcionalidades que estão logicamente relacionadas à classe, mas não dependem do estado da instância ou da classe.

### Exemplo Combinado

Para ilustrar ainda mais a diferença entre métodos de classe e métodos estáticos, aqui está um exemplo que inclui ambos:

```python
class Exemplo:
    atributo_classe = 0

    def __init__(self):
        Exemplo.atributo_classe += 1

    @classmethod
    def metodo_de_classe(cls):
        return f'Atributo da classe: {cls.atributo_classe}'

    @staticmethod
    def metodo_estatico(x, y):
        return f'Resultado da soma: {x + y}'

# Criando instâncias
instancia1 = Exemplo()
instancia2 = Exemplo()

# Usando método de classe
print(Exemplo.metodo_de_classe())  # Saída: Atributo da classe: 2

# Usando método estático
print(Exemplo.metodo_estatico(5, 3))  # Saída: Resultado da soma: 8
```

Neste exemplo, `metodo_de_classe` acessa e retorna um atributo da classe, enquanto `metodo_estatico` realiza uma operação sem acessar ou modificar qualquer estado da classe ou das instâncias.