"""A herança em programação orientada a objetos (POO) 
pode ser categorizada em diferentes tipos, dependendo 
da forma como as classes são estruturadas e relacionam-se
 entre si. Em Python, os principais tipos de herança são:
"""
### 1. Herança Simples
"""Herança simples ocorre quando uma classe derivada herda de uma única classe base.
"""
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

### 2. Herança Múltipla
"""Herança múltipla ocorre quando uma classe deriva de mais de uma classe base.
"""
class Mamifero:
    def amamentar(self):
        return "Amamentando"

class Ave:
    def voar(self):
        return "Voando"

class Morcego(Mamifero, Ave):
    pass

morcego = Morcego()
print(morcego.amamentar())  # Saída: Amamentando
print(morcego.voar())  # Saída: Voando


### 3. Herança Multinível
"""Herança multinível ocorre quando uma classe 
deriva de outra classe derivada, formando uma cadeia de herança.
"""
class Animal:
    def mover(self):
        return "Movendo-se"

class Mamifero(Animal):
    def amamentar(self):
        return "Amamentando"

class Cachorro(Mamifero):
    def fazer_som(self):
        return "Au Au!"

### 4. Herança Hierárquica
"""Herança hierárquica ocorre quando múltiplas classes 
derivadas herdam de uma única classe base.
"""
class Animal:
    def mover(self):
        return "Movendo-se"

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"


### 5. Herança Híbrida
"""Herança híbrida é uma combinação de mais de um tipo de 
herança. Por exemplo, pode envolver uma combinação de herança múltipla e multinível.
"""
class Animal:
    def mover(self):
        return "Movendo-se"

class Mamifero(Animal):
    def amamentar(self):
        return "Amamentando"

class Ave(Animal):
    def voar(self):
        return "Voando"

class Morcego(Mamifero, Ave):
    def fazer_som(self):
        return "Screech"

### Conclusão
"""Entender os diferentes tipos de herança ajuda a estruturar 
melhor o código, promovendo reutilização e evitando redundância.
 Em Python, graças à sua flexibilidade, todos esses tipos de herança podem 
ser implementados, permitindo designs de software mais robustos e versáteis."""