"""O processo de instanciamento em Programação Orientada
a Objetos (POO) refere-se à criação de um objeto a
partir de uma classe. Em Python, isso é feito chamando
a classe como se fosse uma função, o que aciona o 
método `__init__` da classe para inicializar o novo objeto.
"""
### Detalhes do Instanciamento

"""1. **Definição da Classe**: Primeiro, você define uma classe com seus atributos e métodos.
2. **Chamada da Classe para Criar um Objeto**: Você cria 
uma instância da classe, passando os parâmetros necessários 
para o método `__init__`.

Vamos detalhar o processo com exemplos baseados nas classes 
`Livro` e `Biblioteca` que definimos anteriormente.
"""
### Classe `Livro`
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"

#### Instanciamento de `Livro`

"""Para criar uma instância da classe `Livro`, você faz o seguinte:
"""
livro1 = Livro("1984", "George Orwell", 1949)

"""- **Chamada da Classe**: `Livro("1984", "George Orwell", 1949)`
  - Isso chama o método `__init__` da classe `Livro`.
- **Execução do `__init__`**:
  - `self` é a referência ao novo objeto que está sendo criado.
  - `self.titulo` é definido como `"1984"`.
  - `self.autor` é definido como `"George Orwell"`.
  - `self.ano_publicacao` é definido como `1949`.
- **Resultado**: Uma nova instância de `Livro` é criada e armazenada na variável `livro1`.
"""
### Classe `Biblioteca`
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


#### Instanciamento de `Biblioteca`

"""Para criar uma instância da classe `Biblioteca`, você faz o seguinte:
"""
biblioteca = Biblioteca()

"""- **Chamada da Classe**: `Biblioteca()`
  - Isso chama o método `__init__` da classe `Biblioteca`.
- **Execução do `__init__`**:
  - `self` é a referência ao novo objeto que está sendo criado.
  - `self.livros` é inicializado como uma lista vazia.
- **Resultado**: Uma nova instância de `Biblioteca` é criada e armazenada na variável `biblioteca`.
"""
### Exemplos Completos de Uso

"""Vamos ver um exemplo completo combinando a criação de instâncias das duas classes e utilizando seus métodos:
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

### Explicação Final

"""- **Instanciar um Objeto**: Chamar uma classe como se fosse 
uma função, passando os parâmetros necessários para o método `__init__`.
- **Uso de Métodos**: Uma vez instanciados, os métodos dos 
objetos podem ser chamados para manipular e interagir com os 
atributos e outros métodos do objeto.

Compreender o processo de instanciamento é fundamental para 
trabalhar com POO, pois permite criar múltiplas instâncias 
de uma classe, cada uma com seus próprios dados e comportamentos independentes."""