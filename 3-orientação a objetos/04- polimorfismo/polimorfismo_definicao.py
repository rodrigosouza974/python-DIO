### Polimorfismo: Definição

"""Polimorfismo é um conceito fundamental em programação orientada a objetos (OOP) que permite que objetos de diferentes classes sejam tratados através da mesma interface. Em outras palavras, polimorfismo permite que métodos com o mesmo nome, mas em diferentes classes, sejam chamados de maneira uniforme. Isso facilita a reutilização de código e a extensão de funcionalidades sem alterar o código existente.

Existem dois tipos principais de polimorfismo:

1. **Polimorfismo em tempo de compilação (ou polimorfismo estático)**: Geralmente alcançado através de sobrecarga de métodos ou operadores.
2. **Polimorfismo em tempo de execução (ou polimorfismo dinâmico)**: Geralmente alcançado através de herança e interfaces, onde a chamada ao método é resolvida durante a execução.
"""
### Exemplos de Polimorfismo

#### 1. Polimorfismo em tempo de execução (Polimorfismo Dinâmico)

"""Este tipo de polimorfismo é implementado usando herança e interfaces. Vamos ver um exemplo em Python.
"""
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Vaca(Animal):
    def fazer_som(self):
        return "Muuu!"

# Função que aceita qualquer objeto que siga a interface Animal
def emitir_som(animal):
    print(animal.fazer_som())

# Uso
animais = [Cachorro(), Gato(), Vaca()]
for animal in animais:
    emitir_som(animal)

# Saída:
# Au au!
# Miau!
# Muuu!

"""Neste exemplo, a função `emitir_som` pode aceitar qualquer objeto que seja uma subclasse de `Animal` e chamar o método `fazer_som` de maneira polimórfica. Cada subclasse de `Animal` implementa seu próprio comportamento para o método `fazer_som`.
"""
#### 2. Polimorfismo em tempo de compilação (Polimorfismo Estático)

"""Polimorfismo estático é alcançado em linguagens que suportam a sobrecarga de métodos. Python não suporta sobrecarga de métodos diretamente, mas podemos alcançar um comportamento semelhante usando valores padrão e argumentos variáveis.
"""
class Calculadora:
    def soma(self, a, b, c=0):
        return a + b + c

# Uso
calc = Calculadora()
print(calc.soma(2, 3))      # Saída: 5
print(calc.soma(2, 3, 4))   # Saída: 9


"""Neste exemplo, o método `soma` da classe `Calculadora` pode aceitar dois ou três argumentos. Dependendo do número de argumentos passados, ele retorna a soma correspondente.
"""
### Polimorfismo com Funções e Métodos Integrados

"""Em Python, muitas funções e métodos integrados são polimórficos. Por exemplo, a função `len()` pode ser usada para obter o comprimento de diferentes tipos de coleções.
"""
print(len("Olá"))      # Saída: 3
print(len([1, 2, 3]))  # Saída: 3
print(len({"a": 1, "b": 2}))  # Saída: 2

### Benefícios do Polimorfismo

"""1. **Reutilização de Código**: Facilita a reutilização de código, pois você pode usar a mesma interface para diferentes tipos de dados.
2. **Flexibilidade e Extensibilidade**: Facilita a adição de novas funcionalidades sem alterar o código existente.
3. **Manutenção**: Torna o código mais fácil de entender e manter, pois promove o uso de interfaces comuns para diferentes tipos de objetos.

Polimorfismo é uma das características principais que tornam a programação orientada a objetos tão poderosa e flexível. Ele permite que você escreva código mais genérico e reutilizável, melhorando a organização e a escalabilidade dos seus projetos."""