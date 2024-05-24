#count(x)

#Descrição: Retorna o número de vezes que o valor x aparece na tupla.

minha_tupla = (1, 2, 2, 3, 4, 2)
contagem = minha_tupla.count(2)
print(contagem)  # Output: 3

#index(x, [start[, end]])

#Descrição: Retorna o índice da primeira ocorrência do valor x na tupla. Pode opcionalmente receber os argumentos start e end para limitar a busca a uma subsequência da tupla.

minha_tupla = (1, 2, 3, 4, 2)
indice = minha_tupla.index(2)
print(indice)  # Output: 1

# Com argumentos start e end
indice = minha_tupla.index(2, 2)
print(indice)  # Output: 4

"""Operações Suportadas por Tuplas

Concatenar Tuplas :Operador + para juntar duas tuplas.
Repetir Tuplas: Operador * para repetir os elementos de uma tupla um número específico de vezes.
Verificar a Presença de um Elemento:Operador in para verificar se um elemento está presente na tupla.
Tamanho da Tupla: Função len() para obter o número de elementos na tupla.
Acessar Elementos por Índice:print(minha_tupla[0])  # Output: 1
Fatiamento:fatia = minha_tupla[1:4]
"""
"""Funções Úteis com Tuplas

max(tupla): Retorna o maior valor da tupla.
min(tupla): Retorna o menor valor da tupla.
sum(tupla): Retorna a soma dos elementos da tupla (funciona apenas para tuplas de números).
sorted(tupla): Retorna uma lista ordenada dos elementos da tupla.

"""

"""não é possível alterar nenhum valor das tuplas"""