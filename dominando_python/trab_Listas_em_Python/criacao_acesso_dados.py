##Criar uma Lista
#Você pode criar uma lista em Python usando colchetes [] e separando os elementos por vírgulas.

# Lista vazia
minha_lista = []

# Lista com alguns elementos
minha_lista = [1, 2, 3, 4, 5]

# Lista com diferentes tipos de dados
minha_lista = [1, "dois", 3.0, True]

# separa cada letra e exibe como elementos sepados
letras = list ("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = [2010, "fiat", 3.0,"saõ paulo" ,True]

#acesso direto
"""a lista é uma sequencia, portanto podemos acessar seus dados utilizando índices.
 contamos o índice de determinada sequencia a partir do zero
"""
minha_lista = [1, 2, 3, 4, 5]
print(minha_lista[0])

# índices negativos

"""
sequências suportam indexação negativa. a contagem começa com -1"""

frutas = ["maçã", "uva","pera","laranja"]
print(frutas[-1])
print(frutas[-3])

#listas aninhadas
"""
listas podem armazenar todos os tipos de objetos python, portanto podemos ter listas que armazenam
outras listas. com isso podemos criar estruturas bidimessionais(tabelas),
 e acessar informando os índices de uma linha e coluna
"""
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matriz[2][2])
print(matriz[0][2])
print(matriz[-1][-1])

# fatiamento
"""
além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência.
para isso basta passar o índice inicial e/ ou final para acessar o conjunto. 
podemos ainda informar quantas posições o cursor deve "pular" no caso.
"""
#O fatiamento (ou slicing) é uma técnica poderosa em Python usada para acessar subsequências de elementos em uma lista, tupla, string ou qualquer outro tipo de dado que suporte indexação. Usando fatiamento, você pode obter partes específicas dessas sequências de maneira simples e eficiente.

### Sintaxe Básica do Fatiamento
"""
A sintaxe básica para fatiamento é:

sequencia[inicio:fim:passo]

- **`inicio`**: índice inicial da subsequência (inclusivo).
- **`fim`**: índice final da subsequência (exclusivo).
- **`passo`**: intervalo entre os índices.
"""
### Exemplos de Fatiamento em Listas

#### Criando uma Lista de Exemplo

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#### Fatiamento Básico

# Obtendo elementos do índice 2 até o índice 5 (exclusivo)
sublista = lista[2:5]
print(sublista)  # Saída: [2, 3, 4]


#### Fatiamento com Índice Inicial e Final Omissos

# Obtendo todos os elementos desde o início até o índice 5 (exclusivo)
sublista = lista[:5]
print(sublista)  # Saída: [0, 1, 2, 3, 4]

# Obtendo todos os elementos do índice 5 até o final
sublista = lista[5:]
print(sublista)  # Saída: [5, 6, 7, 8, 9]


#### Fatiamento com Passo

# Obtendo todos os elementos com um passo de 2
sublista = lista[::2]
print(sublista)  # Saída: [0, 2, 4, 6, 8]

# Obtendo elementos do índice 1 ao índice 8 com um passo de 3
sublista = lista[1:8:3]
print(sublista)  # Saída: [1, 4, 7]


#### Fatiamento com Índices Negativos
#Os índices negativos permitem que você conte os elementos a partir do final da sequência.


# Obtendo os últimos três elementos
sublista = lista[-3:]
print(sublista)  # Saída: [7, 8, 9]

# Fatiamento de toda a lista com passo negativo (inverte a lista)
sublista = lista[::-1]
print(sublista)  # Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


### Fatiamento em Strings

#O fatiamento também pode ser aplicado a strings, pois elas são sequências de caracteres.


texto = "Hello, World!"

# Obtendo uma substring do índice 7 ao 12
substring = texto[7:12]
print(substring)  # Saída: "World"

# Invertendo a string
string_invertida = texto[::-1]
print(string_invertida)  # Saída: "!dlroW ,olleH"


### Considerações Finais
'''
1. **Omissão de Parâmetros**: Se qualquer um dos parâmetros (início, fim, passo) for omitido, Python usará seus valores padrão: `inicio` como 0, `fim` como o comprimento da sequência e `passo` como 1.
2. **Fatiamento com Passo Negativo**: Permite iterar sobre a sequência de trás para frente.
3. **Índices Fora dos Limites**: Não causam erro em Python. Em vez disso, são ajustados automaticamente.

O fatiamento é uma ferramenta versátil que permite manipular sequências de forma eficiente e elegante. É amplamente utilizado em Python para tarefas como subsetting de dados, inversão de sequências e acesso a partes específicas de strings e listas.
'''
# iterar listas
# a forma mais comum para percorrer os dados de uma lista é utilizando o comando for

carros = ['gol', 'fiat', 'mercedes']

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# compreensão de listas
"""
a compreensão de lista oferece uma sintaxe mais curta quando você
deseja: criar uma nova lista base nos vaalores de uma lista existente(filtro)
ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
"""
#filtro versão 1
numeros_filtro =[3,4,45,74,85,78]
pares =[]

for numero in numeros_filtro:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#filtro versão 2 (mais resumida)
pares2 = [numero for numero in numeros_filtro if numero % 2 == 0]
print(pares2)

# modificando valores versão 1
numeros_base =[3,4,45,74,85,78]
quadrado =[]

for numero in numeros_base:
    quadrado.append(numero** 2)
print(quadrado)

# modificando valores versão 2
quadrado2 = [numero ** 2 for numero in numeros_base]
print(quadrado2)


