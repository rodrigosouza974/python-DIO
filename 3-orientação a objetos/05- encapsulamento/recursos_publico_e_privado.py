"""Em Python, os conceitos de recursos públicos e privados referem-se 
à visibilidade dos atributos e métodos dentro de uma classe. Essa 
visibilidade determina se um atributo ou método pode ser acessado 
diretamente fora da classe ou se está restrito ao escopo interno da 
própria classe. Vamos explorar esses conceitos com mais detalhes:
"""
### Recursos Públicos

"""- **Atributos Públicos**: Atributos de uma classe que podem ser acessados diretamente fora da classe.

- **Métodos Públicos**: Métodos de uma classe que podem ser chamados diretamente fora da classe.

Em Python, todos os atributos e métodos são públicos por padrão, a menos que sejam explicitamente definidos como privados.

Exemplo de recurso público em Python:
"""
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca   # Atributo público
        self.modelo = modelo # Atributo público

    def dirigir(self):
        return f"Dirigindo o {self.marca} {self.modelo}"  # Método público

# Criando uma instância de Carro e acessando recursos públicos
meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.marca)       # Saída: Toyota
print(meu_carro.modelo)      # Saída: Corolla
print(meu_carro.dirigir())   # Saída: Dirigindo o Toyota Corolla

### Recursos Privados

"""- **Atributos Privados**: Atributos de uma classe que são acessados apenas dentro da própria classe ou por métodos da classe.

- **Métodos Privados**: Métodos de uma classe que são acessados apenas dentro da própria classe.

Em Python, para definir um recurso como privado, prefixamos seu nome com dois underscores (`__`). Isso indica que o recurso deve ser tratado como privado e não deve ser acessado diretamente fora da classe.

Exemplo de recurso privado em Python:
"""
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular     # Atributo privado
        self.__saldo = saldo         # Atributo privado

    def __verificar_saldo(self):    # Método privado
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def detalhes_conta(self):
        return f"Titular: {self.__titular}, Saldo: {self.__verificar_saldo()}"

# Criando uma instância de ContaBancaria e acessando recursos privados
minha_conta = ContaBancaria("João", 1000)
print(minha_conta.detalhes_conta())   # Saída: Titular: João, Saldo: 1000

# Tentativa de acessar atributo privado diretamente (não recomendado)
# print(minha_conta.__saldo)  # Isso resultará em um erro 'AttributeError'

# Tentativa de chamar método privado diretamente (não recomendado)
# print(minha_conta.__verificar_saldo())  # Isso resultará em um erro 'AttributeError'


### Acessando Recursos Privados

"""- **Atributos Privados**: Embora seja possível acessar atributos privados
 em Python, não é recomendado fazer isso diretamente fora da classe. Em vez disso,
   é mais apropriado fornecer métodos públicos (como `depositar` e `sacar` no 
   exemplo acima) para interagir com esses atributos de forma controlada.

- **Métodos Privados**: Métodos privados são destinados a serem usados 
internamente dentro da classe. Eles não devem ser chamados diretamente 
fora da classe. O Python não impede completamente o acesso a métodos privados,
 mas a convenção é não acessá-los diretamente fora da classe.
"""
### Conclusão

"""Os recursos públicos e privados em Python permitem controlar a visibilidade 
e o acesso aos atributos e métodos de uma classe. Recursos públicos são acessíveis
 diretamente fora da classe, enquanto recursos privados são acessíveis apenas
internamente. É importante seguir as convenções de acesso para escrever 
código mais seguro, encapsulado e fácil de manter."""