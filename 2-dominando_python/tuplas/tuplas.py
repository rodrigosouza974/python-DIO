# criando tuplas
"""
são estruturas de dados muito parecidas com as listas, a principal diferença
é que tuplas são imutáveis enquanto listas são mutáveis. podemos criar tuplas
atráves da classe tuple, ou colocando valores separados por vírgulas  de parenteses.
obs : ao utlizar parenteses nas tuplas coloque uma , no final
"""
frutas =("laranja", "pera", "uva",)
letras =tuple("rodrigo")
numeros =tuple([1,2,3,4])
país =("brasil",)

#acessso direto a tupla
"""a tupla é uma sequência , portanto podemos acessar 
seus dados utilizando índices.contamos o mesmo de 
determinada sequência a partir do zero.
"""
frutas [0]
frutas [-1]

#tuplas  aninhadas
"""
Tuplas aninhadas em Python são tuplas que contêm 
outras tuplas como seus elementos. Isso permite criar estruturas
 de dados mais complexas e hierárquicas
 ex: tabelas bidimensionais(tabelas), acessando informações pelos
 índices de linha e coluna"""

alunos = (
    ("Alice", (90, 85, 88)),
    ("Bob", (78, 81, 79)),
    ("Carol", (92, 89, 94))
)

# Acessando as notas do segundo aluno (Bob)
notas_bob = alunos[1][1]
print(notas_bob)
# Output: (78, 81, 79)

# Calculando a média das notas de cada aluno
for aluno in alunos:
    nome, notas = aluno
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media}")
# Output:
# Alice - Média: 87.66666666666667
# Bob - Média: 79.33333333333333
# Carol - Média: 91.66666666666667

# fatiamento
"""Fatiamento (ou slicing) em Python é uma técnica poderosa que 
permite acessar partes de uma sequência, como listas, strings e
 tuplas. Usando fatiamento, você pode extrair subpartes dessas 
 sequências de forma eficiente. Vamos explorar 
como o fatiamento funciona com tuplas, incluindo tuplas aninhadas.

sintaxe básica
sequencia[inicio:fim:passo]

inicio: O índice onde a fatia começa (inclusivo).
fim: O índice onde a fatia termina (exclusivo).
passo: A diferença entre os índices sucessivos na fatia (opcional).

"""
#Fatiamento Simples
tupla = (0, 1, 2, 3, 4, 5)

# Fatiando do índice 1 ao 4 (excluindo o 4)
fatia = tupla[1:4]
print(fatia)
# Output: (1, 2, 3)

#Usando Passo
tupla = (0, 1, 2, 3, 4, 5)

# Fatiando com passo 2 (pula um elemento)
fatia = tupla[0:6:2]
print(fatia)
# Output: (0, 2, 4)

#Omissão de Índices
"""Se inicio for omitido, a fatia começa do início
da tupla. Se fim for omitido, a fatia vai até o
 final da tupla. Se passo for omitido, assume-se o
   valor 1:

"""
tupla = (0, 1, 2, 3, 4, 5)

# Do início ao índice 4 (exclusivo)
fatia = tupla[:4]
print(fatia)
# Output: (0, 1, 2, 3)

# Do índice 2 ao final
fatia = tupla[2:]
print(fatia)
# Output: (2, 3, 4, 5)

# Fatiando toda a tupla
fatia = tupla[:]
print(fatia)
# Output: (0, 1, 2, 3, 4, 5)

