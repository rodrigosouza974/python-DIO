"""Sim, se você quiser evitar alterar uma lista global
dentro de uma função, você pode utilizar uma lista 
auxiliar dentro da função. Isso é uma prática comum para
preservar o estado original da lista global. Ao trabalhar
com uma cópia da lista dentro da função, qualquer 
modificação será feita na cópia, não afetando a lista global original.
"""
### Exemplo: Evitando Alteração da Lista Global
"""Vamos considerar uma lista global e uma função 
que trabalha com uma cópia dessa lista.
"""
# Lista global
lista_global = [1, 2, 3, 4, 5]

def modificar_lista(lista):
    # Criar uma cópia da lista para evitar modificar a lista global
    lista_auxiliar = lista.copy()
    
    # Modificar a lista auxiliar
    lista_auxiliar.append(6)
    lista_auxiliar.remove(1)
    
    print("Lista auxiliar dentro da função:", lista_auxiliar)
    return lista_auxiliar

# Chamando a função e passando a lista global
resultado = modificar_lista(lista_global)

# Verificando as listas
print("Lista global após chamada da função:", lista_global)
print("Resultado da função:", resultado)

### Explicação

"""1. **Lista Global**: `lista_global` é definida fora de qualquer
 função, portanto é global.
2. **Função `modificar_lista`**: Esta função aceita uma lista como argumento.
3. **Cópia da Lista**: `lista_auxiliar = lista.copy()` cria 
uma cópia superficial da lista passada como argumento. Isso 
garante que `lista_auxiliar` seja uma lista separada,
 independente de `lista_global`.
4. **Modificação da Lista Auxiliar**: Alterações são feitas 
em `lista_auxiliar`, não afetando `lista_global`.
5. **Retorno da Lista Modificada**: A função retorna a lista auxiliar modificada.
6. **Impressões**: Verificamos que `lista_global` permanece 
inalterada após a chamada da função.
"""
### Output do Exemplo
"""
Lista auxiliar dentro da função: [2, 3, 4, 5, 6]
Lista global após chamada da função: [1, 2, 3, 4, 5]
Resultado da função: [2, 3, 4, 5, 6]
"""
### Mais Sobre Cópias de Listas

#### Cópia Superficial vs Cópia Profunda
"""- **Cópia Superficial (`copy()`)**: Cria uma nova lista,
 mas os elementos dentro da nova lista são referências aos 
 mesmos objetos dentro da lista original.

- **Cópia Profunda (`deepcopy()`)**: Cria uma nova lista e 
recursivamente copia todos os objetos dentro da lista original.
 Para usar `deepcopy`, você precisa importar o módulo `copy`.
"""
#### Exemplo de Cópia Profunda
import copy

lista_global = [[1, 2], [3, 4]]

def modificar_lista(lista):
    # Criar uma cópia profunda da lista para evitar modificar a lista global
    lista_auxiliar = copy.deepcopy(lista)
    
    # Modificar a lista auxiliar
    lista_auxiliar[0].append(3)
    
    print("Lista auxiliar dentro da função:", lista_auxiliar)
    return lista_auxiliar

resultado = modificar_lista(lista_global)

print("Lista global após chamada da função:", lista_global)
print("Resultado da função:", resultado)

### Output do Exemplo de Cópia Profunda
"""Lista auxiliar dentro da função: [[1, 2, 3], [3, 4]]
Lista global após chamada da função: [[1, 2], [3, 4]]
Resultado da função: [[1, 2, 3], [3, 4]]


Usar uma lista auxiliar dentro de uma função para evitar 
modificar a lista global é uma prática recomendada para
 manter a integridade dos dados e evitar efeitos 
 colaterais indesejados."""