Uma classe abstrata é uma classe que não pode ser instanciada diretamente e serve como uma base para outras classes. Ela define um conjunto de métodos e/ou propriedades que devem ser implementados pelas classes derivadas. Em Python, as classes abstratas são criadas usando o módulo `abc` (Abstract Base Classes).

### Características das Classes Abstratas

1. **Não pode ser instanciada:** Você não pode criar uma instância de uma classe abstrata diretamente.
2. **Métodos abstratos:** Pode conter métodos abstratos, que são métodos declarados mas não implementados. As classes derivadas são obrigadas a implementar esses métodos.
3. **Métodos concretos:** Pode também conter métodos concretos, que são métodos completamente implementados.
4. **Herança:** É usada como uma base para outras classes que implementam os métodos abstratos definidos.

### Por que usar classes abstratas?

- **Definir um contrato:** As classes abstratas permitem definir um contrato para as subclasses. Qualquer classe que herde de uma classe abstrata deve implementar os métodos abstratos definidos, garantindo consistência na interface das subclasses.
- **Reutilização de código:** Pode fornecer implementações padrão para alguns métodos, que podem ser reutilizados por várias subclasses.
- **Organização:** Ajuda a organizar o código, especialmente em projetos grandes, promovendo um design claro e consistente.

### Como criar uma classe abstrata em Python

Em Python, você usa o módulo `abc` e o decorador `@abstractmethod` para definir métodos abstratos.

#### Exemplo básico de classe abstrata

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

#### Implementando a classe abstrata

Vamos criar subclasses que herdam da classe abstrata `Animal` e implementam os métodos abstratos.

class Dog(Animal):
    def make_sound(self):
        print("Bark")
    
    def move(self):
        print("Run")

class Fish(Animal):
    def make_sound(self):
        print("Blub")
    
    def move(self):
        print("Swim")

#### Usando as subclasses
dog = Dog()
dog.make_sound()  # Output: Bark
dog.move()        # Output: Run

fish = Fish()
fish.make_sound()  # Output: Blub
fish.move()        # Output: Swim

### Métodos concretos em classes abstratas
Uma classe abstrata pode também conter métodos concretos, que fornecem uma implementação padrão.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
        print("Sleeping...")
```

As subclasses podem usar esses métodos concretos diretamente ou substituí-los se necessário.

```python
class Dog(Animal):
    def make_sound(self):
        print("Bark")
    
    def move(self):
        print("Run")

    def sleep(self):
        print("Dog is sleeping...")

dog = Dog()
dog.make_sound()  # Output: Bark
dog.move()        # Output: Run
dog.sleep()       # Output: Dog is sleeping...
```

### Resumo

Uma classe abstrata em Python é uma maneira de definir um contrato para as subclasses. Ela pode conter métodos abstratos, que devem ser implementados pelas subclasses, e métodos concretos, que podem ser utilizados ou substituídos. As classes abstratas ajudam a organizar o código, garantem consistência na interface das classes e promovem a reutilização de código. Em Python, você pode definir classes abstratas usando o módulo `abc` e o decorador `@abstractmethod`.

Claro! Vamos usar um exemplo da vida real para ilustrar o conceito de classes abstratas. Pense em um sistema de gerenciamento de veículos para uma empresa de transporte. Temos diferentes tipos de veículos, como carros, caminhões e bicicletas, que compartilham algumas características e comportamentos, mas cada um tem suas especificidades.


###exemplo da vida real

### Classe Abstrata: Veículo

Primeiro, definimos uma classe abstrata `Veiculo` que serve como base para todos os tipos de veículos. Nessa classe, declaramos métodos que todos os veículos devem ter, mas que serão implementados de forma específica por cada tipo de veículo.

#### Classe Abstrata

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def dirigir(self):
        pass
    
    @abstractmethod
    def abastecer(self):
        pass
```

### Subclasses: Carro, Caminhão e Bicicleta

Agora, vamos criar subclasses para cada tipo de veículo, implementando os métodos definidos na classe abstrata `Veiculo`.

#### Carro

```python
class Carro(Veiculo):
    def dirigir(self):
        print("Dirigindo um carro")
    
    def abastecer(self):
        print("Abastecendo o carro com gasolina")
```

#### Caminhão

```python
class Caminhão(Veiculo):
    def dirigir(self):
        print("Dirigindo um caminhão")
    
    def abastecer(self):
        print("Abastecendo o caminhão com diesel")
```

#### Bicicleta

```python
class Bicicleta(Veiculo):
    def dirigir(self):
        print("Pedalando uma bicicleta")
    
    def abastecer(self):
        print("Não é necessário abastecer uma bicicleta")
```

### Usando as Subclasses

Agora, podemos criar instâncias de cada tipo de veículo e usar os métodos definidos.

```python
carro = Carro()
caminhao = Caminhão()
bicicleta = Bicicleta()

carro.dirigir()       # Output: Dirigindo um carro
carro.abastecer()     # Output: Abastecendo o carro com gasolina

caminhao.dirigir()    # Output: Dirigindo um caminhão
caminhao.abastecer()  # Output: Abastecendo o caminhão com diesel

bicicleta.dirigir()   # Output: Pedalando uma bicicleta
bicicleta.abastecer() # Output: Não é necessário abastecer uma bicicleta
```

### Explicação para Leigos

- **Classe Abstrata (Veiculo):** Pense na classe `Veiculo` como uma ideia geral do que é um veículo. Sabemos que qualquer veículo pode ser dirigido e, em alguns casos, abastecido. Mas como exatamente isso é feito depende do tipo específico de veículo. Por isso, na classe `Veiculo`, dizemos que todos os veículos devem poder "dirigir" e "abastecer", mas não explicamos como.

- **Subclasses (Carro, Caminhão, Bicicleta):** Agora, imagine que estamos criando tipos específicos de veículos. Um carro, um caminhão e uma bicicleta são todos veículos, mas cada um tem sua maneira de ser dirigido e abastecido. Então, para cada um desses veículos, implementamos a forma específica de dirigir e abastecer.

- **Uso das Subclasses:** Finalmente, quando usamos essas classes específicas (carro, caminhão, bicicleta), podemos chamar os métodos "dirigir" e "abastecer" e ver como cada veículo executa essas ações de maneira própria.

Este exemplo ajuda a entender como classes abstratas e subclasses funcionam na programação, usando uma analogia com veículos, algo comum no nosso dia a dia.


#### porque usar a classe abstrata?

Entendo a confusão, e a pergunta é válida. O conceito de uma classe abstrata pode parecer desnecessário à primeira vista, mas ele tem um propósito específico e importante em design de software, especialmente em programação orientada a objetos. Vamos explorar por que usamos classes abstratas e quais são as vantagens, usando um exemplo da vida real.

### Por que usar uma classe abstrata?

1. **Definir um contrato:** Uma classe abstrata permite definir um conjunto de métodos que todas as subclasses devem implementar. Isso garante que qualquer classe derivada terá uma interface consistente, mesmo que a implementação desses métodos varie.

2. **Reutilização de código:** Se há métodos comuns que várias subclasses podem compartilhar, você pode implementá-los na classe abstrata. Isso evita a duplicação de código e facilita a manutenção.

3. **Polimorfismo:** Classes abstratas permitem que você trate diferentes subclasses de maneira uniforme. Você pode escrever código que opere em objetos da classe abstrata sem se preocupar com a classe específica da instância.

### Exemplo para esclarecer

Vamos usar o exemplo de um sistema de pagamento. Imagine que você está criando um sistema que suporta diferentes métodos de pagamento: cartão de crédito, PayPal e transferência bancária. Cada método de pagamento tem uma forma específica de processar o pagamento, mas todos devem ter um método `processar_pagamento`.

#### Classe Abstrata

Definimos uma classe abstrata `MetodoPagamento` que declara o método `processar_pagamento`.

```python
from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass
```

#### Subclasses

Agora, criamos subclasses para cada método de pagamento, implementando o método `processar_pagamento` de maneira específica.

##### CartaoCredito

```python
class CartaoCredito(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} com cartão de crédito")
```

##### PayPal

```python
class PayPal(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} com PayPal")
```

##### TransferenciaBancaria

```python
class TransferenciaBancaria(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor} via transferência bancária")
```

#### Uso das Subclasses

Você pode tratar todos os métodos de pagamento de maneira uniforme, mesmo que a implementação específica de `processar_pagamento` varie.

```python
def realizar_pagamento(metodo: MetodoPagamento, valor):
    metodo.processar_pagamento(valor)

cartao = CartaoCredito()
paypal = PayPal()
transferencia = TransferenciaBancaria()

realizar_pagamento(cartao, 100.0)       # Output: Processando pagamento de R$100.0 com cartão de crédito
realizar_pagamento(paypal, 150.0)       # Output: Processando pagamento de R$150.0 com PayPal
realizar_pagamento(transferencia, 200.0) # Output: Processando pagamento de R$200.0 via transferência bancária
```

### Vantagens em resumo

1. **Consistência:** Garante que todas as subclasses implementem os métodos necessários.
2. **Reutilização de código:** Métodos comuns podem ser definidos na classe abstrata.
3. **Polimorfismo:** Permite tratar diferentes subclasses de maneira uniforme.

### Conclusão

Embora possa parecer mais fácil chamar diretamente métodos específicos de cada classe, usar classes abstratas fornece uma estrutura clara e consistente, especialmente em sistemas complexos. Isso facilita a manutenção do código, promove a reutilização e garante que as subclasses implementem métodos essenciais de maneira uniforme. A classe abstrata, portanto, não é apenas sobre chamar métodos, mas sobre estruturar e organizar seu código de uma maneira que seja sustentável e escalável a longo prazo.