"""A herança é um dos pilares fundamentais da 
programação orientada a objetos (POO) e permite 
que uma classe (chamada de classe derivada ou subclasse)
herde atributos e métodos de outra classe (chamada de
classe base ou superclasse). Em Python, a herança
permite reutilizar código, estender funcionalidades 
e promover um design mais organizado e modular.
"""
### Exemplo de Herança em Python

# Definindo a classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

# Definindo a classe derivada que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

# Definindo outra classe derivada que herda de Animal
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Criando instâncias das classes derivadas
cachorro = Cachorro("Rex")
gato = Gato("Felix")

print(cachorro.nome)  # Saída: Rex
print(cachorro.fazer_som())  # Saída: Au Au!
print(gato.nome)  # Saída: Felix
print(gato.fazer_som())  # Saída: Miau!

### Explicação do Exemplo

"""1. **Classe Base (`Animal`)**:
   - A classe `Animal` é a superclasse que define um construtor `__init__` para inicializar o nome do animal.
   - Também define um método `fazer_som`, que é um método abstrato (neste caso, sem implementação específica).

2. **Classe Derivada (`Cachorro` e `Gato`)**:
   - `Cachorro` e `Gato` são subclasses de `Animal` e herdam seu comportamento.
   - Cada subclasse implementa o método `fazer_som` de maneira específica.

3. **Criação de Instâncias**:
   - As instâncias `cachorro` e `gato` são criadas a partir das classes `Cachorro` e `Gato`, respectivamente.
   - O nome do animal é inicializado através do construtor herdado da classe `Animal`.
   - Cada instância pode chamar o método `fazer_som`, que foi definido especificamente para cada subclasse.
"""
### Herança Múltipla

"""Python também suporta herança múltipla, onde uma 
classe pode herdar de mais de uma superclasse. Isso 
pode ser útil, mas deve ser usado com cuidado devido 
à complexidade adicional.
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


"""Neste exemplo, a classe `Morcego` herda de duas 
superclasses: `Mamifero` e `Ave`, e pode usar métodos de ambas.
"""
### Conclusão

"""A herança em Python é uma ferramenta poderosa para promover a 
reutilização de código e a organização lógica do programa. Compreender
 como e quando usar a herança pode melhorar significativamente a 
 qualidade e a manutenção do seu código."""