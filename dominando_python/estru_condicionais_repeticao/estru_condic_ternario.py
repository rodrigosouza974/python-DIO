# if ternário

'''
o if ternário permite  escrever uma condição em uma única linha.
ele. é composto por 3 partes,
a 1 parte é o retorno caso a expressão retorne verdadeiro,
a 2 parte é a expressão lógica e 
a 3 parte é o retorno caso a expressão não seja atendida.
'''

saldo = 200
saque = 300
status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao  realizar o saque!")