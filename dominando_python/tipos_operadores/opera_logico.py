# operadores lógicos

# operador E

saldo = 1000
saque = 200
limite = 100

resultado = saldo >= saque and saque <= limite
print("O resultado da expressão de operador E é:", resultado)


# operador OU

saldo = 1000
saque = 200
limite = 100

resultado = saldo >= saque or saque <= limite
print("O resultado da expressão de operador OU é:", resultado)

# operador Negação

saldo = 1000
saque = 200

resultado1 =  not saldo > saque 
print("O resultado da expressão de operador Negação é:", resultado1)

contatos_emergencia =[]
not contatos_emergencia
#true , pois lista vazia em python é considerado false

not "saque 500"
#false , pois a string está prenchida e é considerada verdadeira

not ""
#true , pois a string está vazia e é considerada falsa