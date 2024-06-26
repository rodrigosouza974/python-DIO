"""Em Python, há uma distinção importante entre variáveis de classe e 
variáveis de instância. Cada uma tem seu propósito e escopo específicos.
 Vamos explorar as diferenças:
"""
### Variáveis de Instância

"""
- **Definição**: Variáveis de instância são variáveis que pertencem 
a cada instância de uma classe.
- **Escopo**: Elas são únicas para cada instância da classe.
- **Declaração**: Geralmente são declaradas dentro do método `__init__` usando `self`.
- **Uso**: Cada objeto criado a partir da classe tem sua própria cópia dessas variáveis.
"""
#**Exemplo**:
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Criando duas instâncias da classe Car
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Cada carro tem suas próprias variáveis de instância
print(car1.make)  # Saída: Toyota
print(car2.make)  # Saída: Honda

### Variáveis de Classe

"""
- **Definição**: Variáveis de classe são variáveis que são compartilhadas 
por todas as instâncias de uma classe.
- **Escopo**: Elas pertencem à própria classe e são comuns a todas as instâncias.
- **Declaração**: São declaradas dentro da definição da classe, fora de qualquer método.
- **Uso**: Todas as instâncias da classe compartilham a mesma variável.
"""
#**Exemplo**:
class Car:
    # Variável de classe
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

# Criando duas instâncias da classe Car
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Ambas as instâncias compartilham a variável de classe
print(car1.wheels)  # Saída: 4
print(car2.wheels)  # Saída: 4

# Modificando a variável de classe
Car.wheels = 6

# A modificação afeta todas as instâncias
print(car1.wheels)  # Saída: 6
print(car2.wheels)  # Saída: 6


### Diferenças Principais

"""- **Escopo e Compartilhamento**: Variáveis de instância são específicas 
para cada instância da classe, enquanto variáveis de classe são compartilhadas
 por todas as instâncias.
- **Declaração e Inicialização**: Variáveis de instância são normalmente 
inicializadas no método `__init__`, enquanto variáveis de classe são inicializadas
 diretamente na definição da classe.
- **Acesso**: Variáveis de instância são acessadas usando `self`, enquanto 
variáveis de classe podem ser acessadas usando o nome da classe ou `self`.
"""
### Resumo

"""- **Variáveis de Instância**: São específicas para cada objeto e são definidas
 usando `self` no método `__init__`.
- **Variáveis de Classe**: São comuns a todas as instâncias da classe e são definidas
 diretamente na classe.
"""
"""Compreender essas diferenças é crucial para o design eficiente de classes e objetos
 em Python, permitindo o controle adequado sobre o estado e o comportamento dos objetos."""