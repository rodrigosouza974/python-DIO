Em Python, o decorador `@property` é utilizado para definir métodos que atuam como atributos de uma classe. Ele permite que você controle o acesso a um atributo privado de maneira mais elegante, sem expor diretamente o atributo. Vamos ver um exemplo simples para ilustrar como o `@property` funciona:

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # atributo privado

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.deleter
    def nome(self):
        del self._nome

# Usando a classe
pessoa = Pessoa('João')
print(pessoa.nome)  # Acessando o atributo como se fosse público

pessoa.nome = 'Maria'  # Modificando o atributo com o setter
print(pessoa.nome)

del pessoa.nome  # Deletando o atributo com o deleter
```

Neste exemplo, a classe `Pessoa` possui um atributo privado `_nome`. O decorador `@property` é usado para criar um método `nome` que retorna o valor de `_nome`. Também criamos um setter e um deleter para permitir a modificação e a exclusão do atributo `_nome`.

Essa abordagem proporciona uma maneira mais controlada e segura de acessar e modificar atributos, mantendo a interface pública da classe simples e intuitiva.


Claro, aqui está um exemplo mais complexo que ilustra o uso do `@property` em uma classe que representa uma conta bancária. Essa classe terá atributos como saldo, titular da conta e métodos para depositar, sacar e transferir dinheiro entre contas:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
        if isinstance(novo_titular, str) and novo_titular:
            self._titular = novo_titular
        else:
            raise ValueError("O titular deve ser um nome não vazio.")

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, quantia):
        if quantia > 0:
            self._saldo += quantia
        else:
            raise ValueError("A quantia do depósito deve ser positiva.")

    def sacar(self, quantia):
        if 0 < quantia <= self._saldo:
            self._saldo -= quantia
        else:
            raise ValueError("Quantia de saque inválida ou saldo insuficiente.")

    def transferir(self, outra_conta, quantia):
        if isinstance(outra_conta, ContaBancaria):
            self.sacar(quantia)
            outra_conta.depositar(quantia)
        else:
            raise ValueError("A conta de destino deve ser uma instância de ContaBancaria.")

# Usando a classe ContaBancaria
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)

print(f"Saldo inicial de Alice: {conta1.saldo}")
print(f"Saldo inicial de Bob: {conta2.saldo}")

# Depositando dinheiro
conta1.depositar(200)
print(f"Saldo de Alice após depósito: {conta1.saldo}")

# Sacando dinheiro
conta2.sacar(100)
print(f"Saldo de Bob após saque: {conta2.saldo}")

# Transferindo dinheiro
conta1.transferir(conta2, 150)
print(f"Saldo de Alice após transferência: {conta1.saldo}")
print(f"Saldo de Bob após receber transferência: {conta2.saldo}")

# Alterando o titular da conta
conta1.titular = "Charlie"
print(f"Novo titular da conta1: {conta1.titular}")
```

Neste exemplo, a classe `ContaBancaria` possui:

- Um atributo privado `_titular` para o nome do titular da conta.
- Um atributo privado `_saldo` para o saldo da conta.
- Um método `@property` para obter o titular da conta e um setter para alterar o titular, garantindo que o nome seja uma string não vazia.
- Um método `@property` para obter o saldo da conta.
- Métodos `depositar`, `sacar` e `transferir` para manipular o saldo da conta, com validações adequadas para evitar operações inválidas.

Isso ilustra como o `@property` pode ser usado para controlar o acesso e a modificação de atributos em um cenário mais realista.