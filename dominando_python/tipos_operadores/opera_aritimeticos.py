# operadores executam operadorações matemáticos
# adição
print(5+3)

# subtração
print(10-3)

# multiplicação
print(54*3)

# divisão
print(5/3)

# divisão inteira
print(5//3)

# módulo
print(5%3)

# exponeciação
print(5**3)

# precedencia de operações

"""
Em Python, a precedência dos operadores determina a ordem em que as operações 
são realizadas em expressões complexas. Operadores com maior precedência são 
avaliados primeiro. Aqui está uma lista dos operadores com suas precedências, 
do mais alto para o mais baixo:

1. Parênteses: `()`
2. Potência: `**`
3. Unário positivo e negativo: `+x`, `-x`
4. Multiplicação, divisão, e resto: `*`, `/`, `//`, `%`
5. Adição e subtração: `+`, `-`
6. Operadores de deslocamento: `<<`, `>>`
7. Operadores bit a bit: `&`, `|`, `^`
8. Comparadores: `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `is not`, `in`, `not in`
9. Operadores lógicos: `not`, `and`, `or`

Quando há operadores com a mesma precedência, a ordem de avaliação é normalmente 
da esquerda para a direita, exceto no caso de exponenciação (`**`), que é 
avaliado da direita para a esquerda.

Por exemplo, na expressão `2 + 3 * 4`, a multiplicação é avaliada primeiro 
devido à sua maior precedência, resultando em `2 + 12`, que é igual a `14`.

No entanto, é sempre uma boa prática usar parênteses para tornar explícita 
a ordem de avaliação, especialmente em expressões complexas, para evitar 
ambiguidades e garantir a legibilidade do código.
"""

# exemplos

print(10 - 5 * 2) # resultado = 0

print((10 -5) *2) # resultado = 10

print(10 ** 2 *2) # resultado = 200
