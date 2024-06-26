#como criar conjuntos
#criando sets
"""
um set é uma coleção que não possui objetos repetidos,
usamos sets para representar conjuntos matmáticos ou
eliminar itens duplicados de um interável."""
# De uma lista
lista = [1, 2, 2, 3, 4]
meu_set = set(lista)
print(meu_set)  # Output: {1, 2, 3, 4}

# De uma tupla
tupla = (1, 2, 3, 2)
meu_set = set(tupla)
print(meu_set)  # Output: {1, 2, 3}

# De uma string
string = "hello"
meu_set = set(string)
print(meu_set)  # Output: {'h', 'e', 'l', 'o'}
