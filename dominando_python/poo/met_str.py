"""O método `__str__` em Python é um método especial que define a 
representação em string de um objeto. Quando você implementa o 
`__str__` em uma classe, você está dizendo ao Python como deve ser
a string que representa uma instância dessa classe quando você, por exemplo, imprime a instância.
"""
### Como o `__str__` Funciona

"""O método `__str__` é invocado quando você usa a função `print()` 
em um objeto ou quando converte um objeto em uma string usando a 
função `str()`. Ele deve retornar uma string que represente o objeto
de uma forma legível e amigável."""

### Exemplo com a Classe `Livro`

#Vamos dar uma olhada na classe `Livro` com o método `__str__`:
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"

#### Como o `__str__` é Usado

#1. **Criação de uma Instância de `Livro`**:

livro1 = Livro("1984", "George Orwell", 1949)

#2. **Imprimindo a Instância**:

#Quando você faz `print(livro1)`, o Python chama automaticamente o método `__str__` dessa instância:

print(livro1)

""" saída será:

'1984' por George Orwell (1949)
"""
### Implementação e Uso do `__str__` em Outra Classe

"""Vamos adicionar o método `__str__` à classe `Biblioteca` para que 
possamos imprimir uma representação amigável da biblioteca.
"""
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

#### Usando o `__str__` na Classe `Biblioteca`

#1. **Criação da Instância de `Biblioteca` e Adição de Livros**:
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

#2. **Imprimindo a Instância de `Biblioteca`**:

#Quando você faz `print(biblioteca)`, o Python chama automaticamente o método `__str__` dessa instância:

print(biblioteca)

"""A saída será algo como:
Biblioteca com os seguintes livros: '1984' por George Orwell (1949),
'O Senhor dos Anéis' por J.R.R. Tolkien (1954), 'O Morro dos Ventos Uivantes' por Emily Brontë (1847)
"""
### Resumo

"""- **Método `__str__`**: Define uma representação em string legível de um objeto.
- **Uso**: Chamado automaticamente por `print()` e `str()`.
- **Implementação**: Deve retornar uma string que representa o objeto de maneira amigável e informativa.

O método `__str__` é muito útil para facilitar a depuração e fornecer representações claras dos objetos ao interagir com eles."""