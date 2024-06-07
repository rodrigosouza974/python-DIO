O método construtor `__init__` em Python é um método especial utilizado para inicializar uma nova instância de uma classe. Quando você cria uma nova instância de uma classe, o Python chama automaticamente o método `__init__` dessa classe. Este método permite configurar os atributos iniciais do objeto.

### Funcionamento do `__init__`

- **Nome do Método**: `__init__`
- **Execução**: É chamado automaticamente quando uma nova instância da classe é criada.
- **Parâmetros**: O primeiro parâmetro deve ser `self`, que representa a instância que está sendo criada. Os parâmetros subsequentes são aqueles que você deseja passar ao criar a instância.

### Exemplo com a Classe `Livro`

Vamos revisar a classe `Livro` com o método `__init__`:

```python
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"
```

#### Componentes do Método `__init__`:

1. **Definição do Método**: `def __init__(self, titulo, autor, ano_publicacao):`
    - `self`: Referência à instância que está sendo criada.
    - `titulo`, `autor`, `ano_publicacao`: Parâmetros que serão utilizados para inicializar os atributos da instância.

2. **Inicialização dos Atributos**:
    ```python
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    ```
    - `self.titulo`: Atribui o valor do parâmetro `titulo` ao atributo `titulo` da instância.
    - `self.autor`: Atribui o valor do parâmetro `autor` ao atributo `autor` da instância.
    - `self.ano_publicacao`: Atribui o valor do parâmetro `ano_publicacao` ao atributo `ano_publicacao` da instância.

#### Criando Instâncias de `Livro`

Para criar uma nova instância de `Livro`, você chama a classe passando os argumentos necessários:

```python
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
```

Aqui, `livro1` e `livro2` são instâncias da classe `Livro` inicializadas com os valores fornecidos.

### Exemplo Completo com a Classe `Biblioteca`

Vamos incluir o método `__init__` na classe `Biblioteca`:

```python
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido da biblioteca.")
                return
        print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                print(livro)

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    def __str__(self):
        if not self.livros:
            return "A biblioteca está vazia."
        else:
            livros_str = ", ".join(str(livro) for livro in self.livros)
            return f"Biblioteca com os seguintes livros: {livros_str}"
```

#### Componentes do Método `__init__` em `Biblioteca`:

1. **Definição do Método**: `def __init__(self):`
    - `self`: Referência à instância que está sendo criada.

2. **Inicialização dos Atributos**:
    ```python
    self.livros = []
    ```
    - `self.livros`: Inicializa o atributo `livros` como uma lista vazia.

#### Criando Instâncias de `Biblioteca`

Para criar uma nova instância de `Biblioteca`, você simplesmente chama a classe:

```python
biblioteca = Biblioteca()
```

Aqui, `biblioteca` é uma instância da classe `Biblioteca` com o atributo `livros` inicializado como uma lista vazia.

### Resumo

- **Método `__init__`**: Utilizado para inicializar uma nova instância de uma classe.
- **`self`**: Referência à instância que está sendo criada.
- **Atributos**: São definidos e inicializados dentro do `__init__` usando os parâmetros passados na criação da instância.

Este método é essencial para configurar os atributos iniciais dos objetos e garantir que cada instância da classe esteja corretamente configurada desde o momento da criação.