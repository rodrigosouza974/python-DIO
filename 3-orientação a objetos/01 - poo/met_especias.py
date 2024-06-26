"""Métodos especiais, também conhecidos como "métodos mágicos" 
ou "dunder methods" (porque seus nomes começam e terminam com
dois sublinhados, "__"), são métodos definidos em uma classe 
que Python chama automaticamente em circunstâncias específicas. 
Esses métodos permitem que você defina como instâncias da classe 
devem se comportar com relação a operações básicas e integradas, 
como adição, subtração, comparação, representação em string, entre outras.
"""
### Exemplos de Métodos Especiais

#Aqui estão alguns exemplos comuns de métodos especiais em Python:

#1. **`__init__(self, ...)`**: Inicializa uma nova instância da classe.
 
class Exemplo:
    def __init__(self, valor):
        self.valor = valor
    

#2. **`__str__(self)`**: Define a representação em string de um objeto (usada por `print()` e `str()`).
class Exemplo:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Exemplo com valor {self.valor}"
    

#3. **`__repr__(self)`**: Define a representação "oficial" de um objeto, usada para depuração.
   
    class Exemplo:
        def __init__(self, valor):
            self.valor = valor

        def __repr__(self):
            return f"Exemplo(valor={self.valor})"
    

#4. **`__eq__(self, other)`**: Define o comportamento da igualdade (==).
    
    class Exemplo:
        def __init__(self, valor):
            self.valor = valor

        def __eq__(self, other):
            return self.valor == other.valor
    

#5. **`__add__(self, other)`**: Define o comportamento da adição (+).
    class Exemplo:
        def __init__(self, valor):
            self.valor = valor

        def __add__(self, other):
            return Exemplo(self.valor + other.valor)
    
#6. **`__len__(self)`**: Define o comportamento da função `len()` em um objeto.
    class Exemplo:
        def __init__(self, lista):
            self.lista = lista

        def __len__(self):
            return len(self.lista)
    
### Implementação de Alguns Métodos Especiais

#Vamos implementar uma classe com alguns desses métodos especiais para ver como eles funcionam juntos.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano_publicacao={self.ano_publicacao})"

    def __eq__(self, other):
        if isinstance(other, Livro):
            return (self.titulo == other.titulo and
                    self.autor == other.autor and
                    self.ano_publicacao == other.ano_publicacao)
        return False

    def __lt__(self, other):
        return self.ano_publicacao < other.ano_publicacao


### Utilizando a Classe `Livro` com Métodos Especiais

#Vamos criar algumas instâncias da classe `Livro` e ver como os métodos especiais funcionam:

livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("1984", "George Orwell", 1949)

# __str__ e __repr__
print(str(livro1))  # '1984' por George Orwell (1949)
print(repr(livro2))  # Livro(titulo='O Senhor dos Anéis', autor='J.R.R. Tolkien', ano_publicacao=1954)

# __eq__
print(livro1 == livro3)  # True
print(livro1 == livro2)  # False

# __lt__
print(livro1 < livro2)  # True (1949 < 1954)


### Resumo

"""- **Métodos especiais**: São métodos com nomes específicos 
e entre duplos sublinhados que Python chama automaticamente em certas situações.
- **Exemplos comuns**: `__init__`, `__str__`, `__repr__`, 
`__eq__`, `__add__`, `__len__`, `__lt__`, entre outros.
- **Utilidade**: Eles permitem personalizar o comportamento 
dos objetos da classe para operações integradas do Python, 
tornando os objetos mais intuitivos e fáceis de usar.

Implementar esses métodos especiais nas suas classes permite que 
suas instâncias se comportem de maneira consistente e natural ao interagir com as operações e funções integradas do Python."""