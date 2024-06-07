"""Programação Orientada a Objetos (POO) é um paradigma 
de programação que utiliza "objetos" - instâncias de classes
- para modelar aspectos do mundo real ou sistemas complexos.
Em Python, isso é feito criando classes que definem
propriedades (atributos) e comportamentos (métodos) dos objetos.

Vamos criar um exemplo simples de um programa em POO em 
Python. Suponha que queremos modelar um sistema de 
gerenciamento de uma biblioteca. Teremos classes para 
`Livro` e `Biblioteca`.
"""
### Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"

### Classe Biblioteca

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
    
### Usando as Classes

"""Vamos criar uma instância da `Biblioteca`, adicionar
 alguns livros, listar os livros e buscar por um livro específico.
"""

# Criação de livros
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847)

# Criação da biblioteca
biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando livros na biblioteca
biblioteca.listar_livros()

# Buscando um livro pelo título
titulo_procurado = "1984"
livro_encontrado = biblioteca.buscar_livro_por_titulo(titulo_procurado)
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado}")
else:
    print(f"Livro '{titulo_procurado}' não encontrado na biblioteca.")

# Removendo um livro da biblioteca
biblioteca.remover_livro("O Senhor dos Anéis")

# Listando livros após a remoção
biblioteca.listar_livros()


### Explicação

"""1. **Classe `Livro`**: Define um livro com título, autor e ano
 de publicação. O método `__str__` é sobrescrito para fornecer uma 
 representação amigável do livro quando ele é impresso.

2. **Classe `Biblioteca`**: Gerencia uma coleção de livros. Métodos incluem:
    - `adicionar_livro`: Adiciona um livro à biblioteca.
    - `remover_livro`: Remove um livro pelo título.
    - `listar_livros`: Lista todos os livros na biblioteca.
    - `buscar_livro_por_titulo`: Busca um livro pelo título.

3. **Uso das Classes**: Cria instâncias de livros e da biblioteca,
adiciona os livros à biblioteca, lista os livros, busca um livro específico e remove um livro.

Este exemplo ilustra como utilizar POO em Python para modelar um 
sistema simples de gerenciamento de biblioteca."""