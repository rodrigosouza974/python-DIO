O decorador `@classmethod` em Python é usado para definir um método de classe, que é um método vinculado à classe e não à instância da classe. Isso significa que você pode chamar um método de classe na própria classe, sem precisar criar uma instância dela. O primeiro parâmetro de um método de classe é `cls`, que é uma referência à classe que está sendo chamada.

Aqui está um exemplo de como usar `@classmethod`:

```python
class MinhaClasse:
    contador = 0

    def __init__(self):
        MinhaClasse.contador += 1

    @classmethod
    def contar_instancias(cls):
        return f"Número de instâncias criadas: {cls.contador}"

# Criando instâncias da classe
instancia1 = MinhaClasse()
instancia2 = MinhaClasse()

# Chamando o método de classe
print(MinhaClasse.contar_instancias())  # Saída: Número de instâncias criadas: 2
```

Neste exemplo:

1. `MinhaClasse` tem um atributo de classe `contador` que conta quantas instâncias foram criadas.
2. O método `__init__` incrementa `contador` sempre que uma nova instância é criada.
3. O método `contar_instancias` é um método de classe, definido com o decorador `@classmethod`. Ele usa `cls` para acessar o atributo de classe `contador`.
4. `contar_instancias` pode ser chamado na classe `MinhaClasse` sem precisar criar uma instância, e ele retorna o número de instâncias criadas.