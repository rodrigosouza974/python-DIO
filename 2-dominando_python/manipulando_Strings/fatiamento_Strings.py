#fatiamento 
'''é uma tecnica para retornar subtrings(partes da string original),
informando inicio(start), fim(stop) e passo(step):[start:stop[,step]]
'''

texto = "Python é uma linguagem de programação incrível"

# Fatiamento para obter os primeiros 6 caracteres
primeiros_seis = texto[:6]
print(primeiros_seis)  # Saída: Python

# Fatiamento para obter os caracteres de 7 a 17 (inclusive)
parte_meio = texto[6:18]
print(parte_meio)  # Saída: é uma ling

# Fatiamento para obter os últimos 10 caracteres
ultimos_dez = texto[-10:]
print(ultimos_dez)  # Saída: incrível

print(texto[0])
print(texto[7])
print(texto[:10])
print(texto[10:1:2])
print(texto[:])
print(texto[::-1])

