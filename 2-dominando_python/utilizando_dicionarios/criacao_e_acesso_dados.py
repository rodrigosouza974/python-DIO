#criando dicionários

"""um dicionário é um conjunto não-ordenado de pares chave: valor,
onde as chaves são unicas em uma dada instância do dicionário.
dicionários são determinados por chaves:{}, e contém uma lista 
de pares chav: valor separada por vírgulas.
"""
#1 Criando Dicionários
meu_dicionario = {}
# ou
meu_dicionario = dict()
print(meu_dicionario)  # Output: {}

#2 Dicionário com Pares Chave-Valor
meu_dicionario = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

#3 Adicionando e Atualizando Valores
meu_dicionario["email"] = "alice@example.com"
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo', 'email': 'alice@example.com'}

meu_dicionario["idade"] = 26
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo', 'email': 'alice@example.com'}

#4 Acessando Valores no Dicionário

print(meu_dicionario["nome"])  # Output: Alice
print(meu_dicionario["idade"])  # Output: 25

#5 Removendo Pares Chave-Valor

del meu_dicionario["cidade"]
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 26, 'email': 'alice@example.com'}

#5.1 Usando pop()
email = meu_dicionario.pop("email")
print(email)  # Output: alice@example.com
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 26}

#5.2 Usando popitem()
#Remove e retorna o último par chave-valor inserido:
ultimo_item = meu_dicionario.popitem()
print(ultimo_item)  # Output: ('idade', 26)
print(meu_dicionario)
# Output: {'nome': 'Alice'}

#5.3 Usando clear()
#Remove todos os pares chave-valor do dicionário:
meu_dicionario.clear()
print(meu_dicionario)  # Output: {}


####Métodos Úteis para Dicionários####

#keys()
#Retorna uma visão das chaves do dicionário:
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
print(meu_dicionario.keys())
# Output: dict_keys(['nome', 'idade', 'cidade'])

#values()
#Retorna uma visão dos valores do dicionário:
print(meu_dicionario.values())
# Output: dict_values(['Alice', 25, 'São Paulo'])

#items()
#Retorna uma visão dos pares chave-valor do dicionário:
print(meu_dicionario.items())
# Output: dict_items([('nome', 'Alice'), ('idade', 25), ('cidade', 'São Paulo')])

#get()
#Retorna o valor para a chave especificada, ou um valor padrão se a chave não existir:
print(meu_dicionario.get("nome"))  # Output: Alice
print(meu_dicionario.get("email", "não disponível"))  # Output: não disponível

#update()
#Atualiza o dicionário com pares chave-valor de outro dicionário ou iterável:
novos_dados = {"email": "alice@example.com", "idade": 26}
meu_dicionario.update(novos_dados)
print(meu_dicionario)
# Output: {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo', 'email': 'alice@example.com'}

####Iterando sobre Dicionários####
"""Você pode iterar sobre as chaves, valores ou pares chave-valor de 
um dicionário:
iterar refere-se ao processo de percorrer elementos de uma coleção,
como listas, tuplas, dicionários, sets, ou outros iteráveis.
Iterar é uma operação fundamental em muitas linguagens de programação 
e é usada para executar um bloco de código repetidamente 
para cada item na coleção."""

#Iterando sobre as Chaves
for chave in meu_dicionario:
    print(chave)
# Output:
# nome
# idade
# cidade
# email

#Iterando sobre os Valores
for valor in meu_dicionario.values():
    print(valor)
# Output:
# Alice
# 26
# São Paulo
# alice@example.com

#Iterando sobre Pares Chave-Valor
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
# Output:
# nome: Alice
# idade: 26
# cidade: São Paulo
# email: alice@example.com

#Exemplos Práticos
#Contando Ocorrências de Caracteres em uma String
string = "abracadabra"
contagem = {}
for char in string:
    if char in contagem:
        contagem[char] += 1
    else:
        contagem[char] = 1
print(contagem)
# Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

#Usando um Dicionário para Representar um Contato
contato = {
    "nome": "Bob",
    "telefone": "1234-5678",
    "email": "bob@example.com"
}
print(contato)
# Output: {'nome': 'Bob', 'telefone': '1234-5678', 'email': 'bob@example.com'}

####Criando um Dicionário Aninhado####
"""podem armazenar qualquer tipo de objeto python
como valor, desde que a chave para esse valor seja
um objeto imutável como (strings e números)"""
alunos = {
    "Alice": {
        "idade": 25,
        "curso": "Engenharia",
        "notas": [90, 85, 88]
    },
    "Bob": {
        "idade": 22,
        "curso": "Matemática",
        "notas": [75, 80, 83]
    },
    "Carol": {
        "idade": 23,
        "curso": "Física",
        "notas": [95, 90, 92]
    }
}
#Acessando Valores em um Dicionário Aninhado
# Acessando a idade de Alice
idade_alice = alunos["Alice"]["idade"]
print(idade_alice)  # Output: 25

# Acessando o curso de Bob
curso_bob = alunos["Bob"]["curso"]
print(curso_bob)  # Output: Matemática

# Acessando as notas de Carol
notas_carol = alunos["Carol"]["notas"]
print(notas_carol)  # Output: [95, 90, 92]
