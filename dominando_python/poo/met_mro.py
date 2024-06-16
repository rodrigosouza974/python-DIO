"""Em Python, MRO (Method Resolution Order) é a ordem na qual os métodos 
são pesquisados em uma hierarquia de classes. Quando você chama um 
método em uma instância de uma classe, Python segue essa ordem para 
encontrar o método correto a ser executado. Isso é especialmente 
importante em casos de herança múltipla.

Para entender melhor, vamos explorar como a MRO funciona e como 
você pode visualizá-la em Python.
"""
### Como Python Determina a MRO?

"""Python usa o algoritmo C3 linearization para determinar a MRO de uma classe. 
Este algoritmo garante que a ordem de resolução seja consistente e que todas as 
classes pai sejam corretamente respeitadas. 
"""
### Exemplo de MRO com Herança Múltipla

#Vamos considerar um exemplo com múltiplas classes para ilustrar isso:

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()

"""Neste exemplo, temos uma hierarquia de classes com herança múltipla
. A classe `D` herda de `B` e `C`, que por sua vez herdam de `A`. 
Quando chamamos `d.show()`, Python precisa determinar qual método `show` chamar.
"""
### Visualizando a MRO
#Podemos usar o método `mro()` para visualizar a MRO de uma classe:

print(D.mro())

"""Isso vai mostrar a ordem na qual Python vai procurar métodos:

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""
### Explicando a Ordem

"""1. **`D`**: Começa pela própria classe `D`.
2. **`B`**: Vai para a primeira classe base, `B`.
3. **`C`**: Como `B` e `C` são irmãos, ele vai para `C` depois.
4. **`A`**: Como `B` e `C` herdam de `A`, ele vai para `A`.
5. **`object`**: Finalmente, chega à classe base mais alta, `object`.
"""
### Exemplo de Uso
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Visualizando a MRO
print(D.mro())

# Testando a chamada do método
d = D()
d.show()

#Quando você executa isso, verá a MRO como listada anteriormente, e a chamada para `d.show()` imprimirá `B` porque `B` aparece antes de `C` na MRO.

### Verificando a MRO com `super()`

#A função `super()` em Python também segue a MRO. Quando você usa `super()`, Python segue a MRO para determinar a próxima classe a ser chamada. Aqui está um exemplo modificado para ilustrar o uso de `super()`:
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

# Testando a chamada do método
d = D()
d.show()

"""A saída será:
D
B
C
A
"""
#Isso demonstra como `super()` segue a MRO para chamar os métodos das classes base na ordem correta.

### Conclusão

"""A MRO em Python é uma característica poderosa que garante que os métodos sejam 
resolvidos de forma consistente e previsível, especialmente em hierarquias de 
classes complexas com herança múltipla. Entender e utilizar a MRO pode ajudar a 
evitar bugs e comportamentos inesperados em seus programas Python."""