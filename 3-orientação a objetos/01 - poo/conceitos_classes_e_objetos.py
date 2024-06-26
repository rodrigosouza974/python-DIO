"""Em Python, os conceitos de classe e objeto são fundamentais na programação orientada 
a objetos (POO). Eles permitem a criação de estruturas de dados complexas e a 
reutilização de código. Vamos explorar esses conceitos com detalhes.
"""
### Classe

"""Uma classe é um modelo ou uma planta que define um conjunto de atributos e métodos
que os objetos criados a partir dessa classe terão. Em Python, uma classe é definida
usando a palavra-chave `class`. """

#### Definindo uma Classe
"""
Aqui está um exemplo básico de uma definição de classe em Python:
"""

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


"""- `class Carro:`: Define uma nova classe chamada `Carro`.
- `def __init__(self, marca, modelo, ano):`: Define o método inicializador (construtor) que é chamado quando um novo objeto da classe é criado. Ele inicializa os atributos da classe.
- `self.marca = marca`: `self` refere-se à instância atual da classe e é usado para acessar variáveis que pertencem à classe.
- `def descricao(self):`: Define um método chamado `descricao` que retorna uma string descritiva do carro.
"""
### Objeto

"""Um objeto é uma instância de uma classe. Quando uma classe é definida, nenhum espaço de memória é alocado até que um objeto dessa classe seja instanciado. Criar um objeto é chamado de "instanciar" a classe.
"""
#### Criando um Objeto

"""Aqui está como você pode criar um objeto da classe `Carro` definida acima:
"""

meu_carro = Carro("Toyota", "Corolla", 2020)

"""Neste exemplo, `meu_carro` é uma instância da classe `Carro`. Você pode 
acessar os atributos e métodos do objeto usando a notação de ponto:
"""

print(meu_carro.marca)  # Output: Toyota
print(meu_carro.descricao())  # Output: Toyota Corolla (2020)

### Mais Sobre Classes e Objetos

#### Atributos de Classe vs. Atributos de Instância

"""
- **Atributos de Instância**: Atributos que são específicos para cada 
instância de uma classe. No exemplo acima, `marca`, `modelo`, e `ano` 
são atributos de instância.
  
- **Atributos de Classe**: Atributos que são compartilhados entre todas
as instâncias de uma classe. Eles são definidos diretamente na classe e 
não no método inicializador.
"""

class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo de instância
        self.modelo = modelo  # Atributo de instância
        self.ano = ano  # Atributo de instância

#### Herança

"""Herança permite criar uma nova classe baseada em uma classe existente.
 A nova classe (classe derivada) herda os atributos e métodos da classe 
 existente (classe base).
"""

class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def mostrar_tipo(self):
        print(f"Tipo do veículo: {self.tipo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__("Carro")
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} ({self.ano})"


"""
Neste exemplo, `Carro` herda da classe `Veiculo`. A função
 `super().__init__("Carro")` chama o inicializador da classe 
 base `Veiculo`.
"""