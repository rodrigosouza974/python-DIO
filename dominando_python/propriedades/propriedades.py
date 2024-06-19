"""O decorador `@property` em Python é uma maneira conveniente de usar métodos 
 como se fossem atributos, proporcionando controle sobre o acesso e a 
 modificação de atributos de instância de uma classe. Ele permite que 
você defina métodos que podem ser acessados como atributos, mantendo a
simplicidade de uso e permitindo validações e cálculos automáticos ao 
acessar ou definir esses valores.
"""
#Aqui está um exemplo básico de como usar `@property`:

### Exemplo 1: Uso básico de `@property`

class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        self._raio = valor

    @property
    def area(self):
        return 3.14159 * (self._raio ** 2)

# Uso
c = Circulo(5)
print(c.raio)  # Acessa o raio usando o método getter
c.raio = 10   # Define o raio usando o método setter
print(c.area)  # Calcula a área automaticamente

# Tentativa de definir um valor negativo
try:
    c.raio = -5
except ValueError as e:
    print(e)  # "O raio não pode ser negativo"

### Explicação do código:

"""1. **Definição da Classe**:
   - A classe `Circulo` tem um atributo privado `_raio`.
   
2. **@property**:
   - O decorador `@property` é usado para definir um método que pode ser acessado como um atributo. No exemplo, `raio` é um método que retorna o valor de `_raio`.

3. **Setter**:
   - `@raio.setter` permite definir um método que é executado quando o atributo `raio` é alterado. Ele faz a verificação se o valor é negativo e lança uma exceção se for.

4. **Getter para área**:
   - `@property` também pode ser usado para métodos que calculam valores derivados, como `area` que calcula a área do círculo com base no raio.
"""
### Vantagens de usar `@property`:

"""1. **Encapsulamento**:
   - Permite encapsular a lógica de validação e cálculo de atributos, mantendo a interface simples para o usuário da classe.

2. **Interface Consistente**:
   - O acesso e modificação de atributos podem ser realizados da mesma forma que acessamos variáveis públicas, mas com a vantagem de adicionar lógica adicional.

3. **Backward Compatibility**:
   - Pode transformar métodos em atributos, melhorando a legibilidade do código sem quebrar a interface existente.
"""
### Exemplo 2: Somente leitura

#Às vezes, você pode querer um atributo que seja somente leitura. Isso pode ser feito omitindo o setter.
class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    @property
    def area(self):
        return self._largura * self._altura

# Uso
r = Retangulo(3, 4)
print(r.area)  # Acessa a área como um atributo
# r.area = 12  # Isso geraria um erro, pois não há um setter definido

"""Neste exemplo, a propriedade `area` é somente leitura, porque não há
 um método setter definido para ela. Isso é útil quando você deseja 
 calcular um valor a partir de outros atributos e não deseja permitir 
 a modificação direta desse valor calculado.

Em resumo, `@property` é uma ferramenta poderosa em Python que ajuda a 
criar classes com interfaces limpas e intuitivas, permitindo ao mesmo tempo 
controle e flexibilidade sobre como os atributos são acessados e modificados."""