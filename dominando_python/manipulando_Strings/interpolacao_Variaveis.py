# Interpolação de variáveis
'''Em python temos 3 formas de interpolar variáveis em string, a primeira
é usando o sinal%, a segunda é utilizando o método format e a ultima e f strings.
a 1 forma não é atualmente recomendada e seu uso em python é raro, por esse motivo iremos focar nas 2 ultimas.
'''


#old style %
nome = "guilherme"
idade = 28
profissao = "programador"
linguagem = "python"

print("Olá, meu nome é %s, tenho %d anos e sou %s em %s." % (nome, idade, profissao, linguagem))


# método format
print("Olá, meu nome é {}, tenho {} anos e sou {} em {}.".format(nome, idade, profissao, linguagem))
print("Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao} em {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao} em {linguagem}.".format(**pessoa))

# método f string

print(f"Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao} em {linguagem}.")

# formatação strings  com f-string
PI = 3.14159
print(f"valor de PI:{PI:.2f}")

print(f"valor de PI:{PI:10.2f}")