Em Python, termos como método, atributo e propriedade têm significados específicos. Aqui está uma explicação detalhada das diferenças entre eles:

### Método

Um método é uma função definida dentro de uma classe e que atua sobre instâncias dessa classe. Métodos podem acessar e modificar os atributos da instância e, geralmente, são usados para definir o comportamento da classe. Os métodos são definidos usando a palavra-chave `def`.

**Exemplo:**
```python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        return f"{self.nome} está latindo!"

meu_cachorro = Cachorro("Rex", 2)
print(meu_cachorro.latir())  # Output: Rex está latindo!
```

### Atributo

Atributos são variáveis que pertencem a uma classe (atributos de classe) ou a uma instância de uma classe (atributos de instância). Eles armazenam dados relativos à classe ou à instância.

**Exemplo:**
```python
class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância

meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.marca)  # Output: Toyota
print(Carro.rodas)  # Output: 4
```

### Propriedade

Propriedades são uma forma de encapsular o acesso aos atributos. Elas permitem adicionar lógica ao acessar ou definir um atributo. Propriedades são definidas usando o decorador `@property` e podem ter métodos getter, setter e deleter.

**Exemplo:**
```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Atributo "privado"

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self._nome = valor
        else:
            raise ValueError("Nome deve ser uma string")
    
    @nome.deleter
    def nome(self):
        del self._nome

pessoa = Pessoa("Ana")
print(pessoa.nome)  # Output: Ana

pessoa.nome = "João"
print(pessoa.nome)  # Output: João

# Se tentar definir um valor não-string, levantará um ValueError
# pessoa.nome = 123  # ValueError: Nome deve ser uma string
```

### Resumo

- **Método:** Função definida dentro de uma classe que atua sobre instâncias dessa classe.
- **Atributo:** Variável que pertence a uma classe ou a uma instância de uma classe.
- **Propriedade:** Forma de encapsular o acesso aos atributos, permitindo adicionar lógica ao acessá-los ou defini-los.

Cada um desses componentes tem um papel específico na estrutura e no comportamento das classes e objetos em Python, permitindo um controle refinado sobre a manipulação de dados e a funcionalidade dos objetos.