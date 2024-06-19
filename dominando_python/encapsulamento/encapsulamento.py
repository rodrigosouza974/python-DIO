"""Em Python, encapsulamento refere-se à prática de restringir o acesso
 direto aos métodos e variáveis de uma classe, a fim de prevenir modificações 
 não autorizadas que possam levar a estados inconsistentes do objeto. Isso é 
 geralmente alcançado usando convenções de nomenclatura e propriedades especiais.

Existem duas principais convenções para indicar o nível de visibilidade de um 
atributo ou método em Python:

1. **Público:** Atributos e métodos que podem ser acessados de fora da classe.
 Isso é feito simplesmente definindo-os sem underscores (`_`) no início.

2. **Privado:** Atributos e métodos que devem ser acessados apenas de dentro
 da própria classe. Isso é indicado prefixando o nome do atributo ou método 
 com dois underscores (`__`).

Por exemplo, vamos criar uma classe simples para demonstrar encapsulamento:
"""

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca       # Atributo público
        self.modelo = modelo     # Atributo público
        self.__quilometragem = 0 # Atributo privado

    def dirigir(self, distancia):
        self.__quilometragem += distancia

    def get_quilometragem(self):
        return self.__quilometragem

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla")
meu_carro.dirigir(100)
print(meu_carro.get_quilometragem())  # Saída: 100

"""Neste exemplo:
- `marca` e `modelo` são atributos públicos que podem ser acessados diretamente de fora da classe.
- `__quilometragem` é um atributo privado. Tentar acessá-lo diretamente fora da 
classe geraria um erro (`AttributeError`).

O encapsulamento em Python não impede completamente o acesso aos atributos
 privados, mas eles são renomeados internamente na forma `_NomeDaClasse__nome_do_atributo`.
   Por exemplo, `__quilometragem` na classe `Carro` se torna `_Carro__quilometragem`.
     No entanto, essa não é uma prática recomendada, pois viola o encapsulamento.

Além disso, Python oferece o conceito de **propriedades** e **decorators** (`property`) 
que podem ser usados para controlar o acesso e modificar o comportamento dos métodos de
 acesso e modificação de atributos, garantindo assim um encapsulamento mais robusto.

Em resumo, encapsulamento em Python é mais uma convenção baseada em nomes do que uma 
regra rígida como em outras linguagens orientadas a objetos, como Java ou C#. A boa 
prática é usar a convenção de nomenclatura e, se necessário, utilizar propriedades 
para controlar o acesso aos atributos privados de forma mais segura."""